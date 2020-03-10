"""
Functions for validating knowledge graphs against biolink model
using KGX and json schema
"""
from typing import List, Union, Dict
from kgx.transformers.rsa_transformer import RsaTransformer
from kgx.validator import Validator, ErrorType, MessageLevel, ValidationError
from dataclasses import asdict
import fastjsonschema
from jsonschema import validate as jsonvalidate
from .models.knowledge_graph import KnowledgeGraph
from .models.message import Message
from .models.errors import TransformationError


def validate_with_kgx(
        data: Union[Dict, KnowledgeGraph, Message]
) -> List[Union[ValidationError, TransformationError]]:
    """
    Validate a rsa knowledge graph with kgx

    First transforms the graph using the RsaTransformer, then
    performs validation with the Validator class
    :param data:
    :return:
    """
    if isinstance(data, Message):
        message = asdict(data)
    elif isinstance(data, KnowledgeGraph):
        message = {
            'knowledge_graph': asdict(data)
        }
    elif 'knowledge_graph' not in data:
        message = {
            'knowledge_graph': data
        }
    else:
        message = data

    biolinkified = RsaTransformer()

    try:
        biolinkified.load(message)
    except KeyError as exc:
        return [
            TransformationError(
                error_type="TransformationError",
                message="Could not transform reasoner "
                        "message into biolink graph: {}".format(str(exc)),
        )]
    validator = Validator(verbose=True)

    return validator.validate(biolinkified.graph)


def validate_with_jsonschema(schema: Dict, data: Union[KnowledgeGraph, Message]):
    #jsonvalidate(instance=data, schema=schema)
    return


def validate_with_fastjsonschema(schema: Dict, data: Union[KnowledgeGraph, Message]):
    #validate = fastjsonschema.compile(schema, data)
    #validate(data)
    return
