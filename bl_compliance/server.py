"""FastAPI BL compliance server."""
import yaml
import requests
import json
from pathlib import Path
from typing import Union, Dict, Any, List
from fastapi import FastAPI, Body
from starlette.responses import JSONResponse
from starlette.requests import Request
from .validator import validate_with_jsonschema, validate_with_kgx
from .models.knowledge_graph import KnowledgeGraph
from .models.message import Message


# Custom exception handler
class BlValidationException(Exception):
    def __init__(self, content: List):
        self.content = content


app = FastAPI(
    title="Biolink Validation Service",
    version="0.0.1",
    description="Utilities for validating a graph object with the BioLink Model",
)

config_path = Path(__file__).parent.parent / 'conf' / 'config.yaml'
config_fh = open(config_path, 'r')
config = yaml.load(config_fh, Loader=yaml.SafeLoader)

example_fh = Path(__file__).parent.parent / 'resources' / 'validate_kg_example.json'

with open(example_fh) as json_data:
    val_kg_example = json.load(json_data)

req = requests.get(config['biolink_model'])
biolink_schema = req.json()


@app.exception_handler(BlValidationException)
async def blvalidation_exception_handler(request: Request, exc: BlValidationException):
    return JSONResponse(
        status_code=418,
        content=[content.as_dict() for content in exc.content],
    )

@app.post('/validate/knowledge_graph', response_model=Dict[Any, Any])
async def validate_knowledge_graph(
        data: Union[KnowledgeGraph, Message] = Body(..., example=val_kg_example)
):
    """
    Validates a knowledge graph against the BioLink model
    """
    #json_validation = validate_with_jsonschema(biolink_schema, data)
    kgx_validation = validate_with_kgx(data)
    if kgx_validation:
        raise BlValidationException(content=kgx_validation)
    return {"message": "Successfully validated"}


@app.get("/version")
async def get_version():
    """
    Get the versions of the Biolink Model JSON schema
    and the Reasoner API standard
    """
    return config
