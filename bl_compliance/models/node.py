from typing import Union, List, Mapping, Any, Optional
from pydantic.dataclasses import dataclass


class Config:
    orm_mode = True


@dataclass(init=False, config=Config)
class Node:
    id: str
    name: Optional[str] = None
    type: Optional[Union[str, List]] = None
    kwargs: Optional[Mapping[Any, Any]] = None

    def __init__(
            self,
            id: str,
            name: Optional[str] = None,
            type: Optional[Union[str, List]] = None,
            **kwargs
    ):
        self.id = id
        self.name = name
        self.type = type
        self.kwargs = kwargs
