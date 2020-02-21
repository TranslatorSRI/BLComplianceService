from typing import Union, List, Mapping, Any, Optional
from pydantic.dataclasses import dataclass


class Config:
    orm_mode = True


@dataclass(init=False, config=Config)
class Edge:
    id: str
    source_id: str
    target_id: str
    type: Optional[Union[str, List]] = None
    kwargs: Optional[Mapping[Any, Any]] = None

    def __init__(
            self,
            id: str,
            source_id: str,
            target_id: str,
            type: Optional[Union[str, List]] = None,
            **kwargs
    ):
        self.id = id
        self.source_id = source_id
        self.target_id = target_id
        self.type = type
        self.kwargs = kwargs
