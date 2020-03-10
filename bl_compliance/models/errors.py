from dataclasses import dataclass


@dataclass()
class TransformationError:
    error_type: str
    message: str

    def as_dict(self):
        return vars(self)
