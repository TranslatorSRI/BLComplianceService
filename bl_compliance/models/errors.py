from dataclasses import dataclass
from kgx.validator import ErrorType, MessageLevel


@dataclass()
class TransformationError:
    error_type: str
    message: str

    def as_dict(self):
        return vars(self)


@dataclass()
class KgxError():
    """
    This will eventually come from KGX
    """
    message_level: MessageLevel
    error_type: ErrorType
    element: str
    error_message: str
    details: str

    def as_dict(self):
        return {
            'message_level': self.message_level.name,
            'error_type': self.message_level.name,
            'element': self.element,
            'error_message': self.error_message,
            'details': self.details
        }
