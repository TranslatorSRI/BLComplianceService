from dataclasses import dataclass


@dataclass()
class TransformationError:
    error_type: str
    message: str
