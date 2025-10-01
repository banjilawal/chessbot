from chess.exception import ChessException, ValidationException, NullException, BuilderException

__all__ = [
    'EventException',
    'NullEventException',
    'InvalidEventException',
    'EventBuilderException'
]


class EventException(ChessException):
    ERROR_CODE = "EVENT_ERROR"
    DEFAULT_MESSAGE = "Event raised an error"

class NullEventException(EventException, NullException):
    ERROR_CODE = "NULL_EVENT_ERROR"
    DEFAULT_MESSAGE = "Event cannot be null"

class InvalidEventException(EventException, ValidationException):
    ERROR_CODE = "INVALID_EVENT_ERROR"
    DEFAULT_MESSAGE = "Event validation failed"

class EventBuilderException(EventException, BuilderException):
    ERROR_CODE = "EVENT_BUILDER_ERROR"
    DEFAULT_MESSAGE = "EventBuilder validation failed"
