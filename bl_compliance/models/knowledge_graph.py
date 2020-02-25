from typing import List, Mapping, Any, Optional, Union
from pydantic.dataclasses import dataclass
from .node import Node
from .edge import Edge


class Config:
    orm_mode = True


@dataclass(init=False, config=Config)
class KnowledgeGraph:
    nodes: List[Node]
    edges: List[Edge]
    kwargs: Optional[Mapping[Any, Any]] = None

    def __init__(
            self,
            nodes: List[Node],
            edges: List[Edge],
            **kwargs
    ):
        self.nodes = nodes
        self.edges = edges
        self.kwargs = kwargs
