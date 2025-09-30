from chess.piece import InvalidPieceException
from chess.exception import ChessException, BuilderException

__all__ = [
    'ActorException',
    'ActorBuilderException',
    'InvalidActorException',
    'RequiredActorNotFoundException',
    'ActorPlacementRequiredException',
    'CapturedActorCannotActException',

    'SubjectException',
    'InvalidSubjectException',
    'RequiredSubjectNotFoundException',
    'SubjectPlacementRequiredException',
    'DoubleCapture'
]

class ActorException(ChessException):
    """
    Superclass for all scan event exceptions. DO NOT USE DIRECTLY. Subclasses give more specific error messages
    useful for debugging.
    """
    ERROR_CODE = "ACTOR_ERROR"
    DEFAULT_MESSAGE = "An Actor exception occurred"


class ActorBuilderException(ActorException, BuilderException):
    """Raised if a builder fails to create an Actor."""
    ERROR_CODE = "ACTOR_BUILDER_ERROR"
    DEFAULT_MESSAGE = "ActorBuilder failed to create an Actor"


class InvalidActorException(ActorException, InvalidPieceException):
    """Raised if an actor fails validation."""
    ERROR_CODE = "ACTOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Required actor failed validation. Event cannot be executed"


class RequiredActorNotFoundException(ActorException):
    """Raised when a potential actor is not found on the  board."""
    ERROR_CODE = "ACTOR_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Required actor was not found on the board. Event cannot be executed"


class ActorPlacementRequiredException(ActorException):
    """Raised when a potential actor has not been placed on the board."""
    ERROR_CODE = "ACTOR_PLACEMENT_REQUIRED_ERROR"
    DEFAULT_MESSAGE = (
        "Required actor has an empty position stack. It as not been placed on the board. Event cannot be executed."
    )


class CapturedActorCannotActException(ActorException):
    """Raised when a captured actor attempts to act on the board."""
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot act on the board. Event cannot be executed"





class SubjectException(ChessException):
    """
    SubjectException classes are raised on a piece acted upon. They are raised on the same errors as ActorException,
    Using SubjectException makes tracing which side of the interaction is raising an error easier.
    """
    ERROR_CODE = "SUBJECT_ERROR"
    DEFAULT_MESSAGE = "A potential subject piece raised an exception"


class InvalidSubjectException(SubjectException, InvalidPieceException):
    """Raised if a required subject fails validation."""
    ERROR_CODE = "SUBJECT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Required subject failed validation. Actor cannot fire event onto subject"


class RequiredSubjectNotFoundException(SubjectException):
    """Raised when a required subject is not found on the  board."""
    ERROR_CODE = "SUBJECT_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Required subject was not found on the board. Actor cannot fire event onto subject"


class SubjectPlacementRequiredException(SubjectException):
    """Raised when a required subject has not been placed on the board."""
    ERROR_CODE = "SUBJET_PLACEMENT_REQUIRED_ERROR"
    DEFAULT_MESSAGE = (
        "Required subject has an empty position stack. It as not been placed on the board. Actor cannot"
        "fire event onto subject."
    )


class DoubleCapture(SubjectException):
    """Raised when an actor tries to capture a piece already imprisoned."""
    ERROR_CODE = "DOUBLE_CAPTURE_ERROR"
    DEFAULT_MESSAGE = "Subject is already captured"





