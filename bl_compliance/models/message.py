from pydantic.dataclasses import dataclass
from typing import List, Mapping, Any, Optional, Dict
from .knowledge_graph import KnowledgeGraph


class Config:
    orm_mode = True


@dataclass(init=False, config=Config)
class Message():
    knowledge_graph: KnowledgeGraph
    results: Optional[List[Any]] = None
    query_graph: Optional[Dict] = None
    kwargs: Optional[Mapping[Any, Any]] = None

    def __init__(
            self,
            knowledge_graph: KnowledgeGraph,
            results: Optional[List[Any]] = None,
            query_graph: Optional[Dict] = None,
            **kwargs
    ):
        self.knowledge_graph = knowledge_graph
        self.results = results
        self.query_graph = query_graph
        self.kwargs = kwargs
