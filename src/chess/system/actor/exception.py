from chess.exception import RollbackException
from chess.piece import PieceException, InvalidPieceException

__all__ = [
    'ActorException',
    'ActorRollBackException',

# === ACTOR VALIDATION EXCEPTIONS ===
    'InvalidActorException',
    'ActorNotOnBoardException',
    'ActorPlacementRequiredException',

# === ACTOR ACTIVITY EXCEPTIONS ===
    'CapturedActorCannotActException',
    'CapturedActorCannotAttackException',
    'CapturedActorCannotMoveException',
    'CheckMatedKingActivityException',

# === SUBJECT ACTIVITY EXCEPTIONS ===
    'SubjectException',
    'InvalidSubjectException',
    'SubjectNotOnBoardException',
    'SubjectPlacementRequiredException'
]

class ActorException(PieceException):
    """
    Super class of all exceptions an actor object can raise. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all piece exceptions
    """
    ERROR_CODE = "ACTOR_ERROR"
    DEFAULT_MESSAGE = "Actor raised an err. Piece cannot act."

class ActorRollBackException(ActorException, RollbackException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "ACTOR_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Actor raised an err. Transaction rolled back"


# === ACTOR VALIDATION EXCEPTIONS ===
class InvalidActorException(ActorException, InvalidPieceException):
    """
    Raised by ActorValidator if piece fails any conditions for acting on the board.
    Exists primarily to catch all exceptions raised validating an existing piece
    """
    ERROR_CODE = "ACTOR_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece did not meet condition to act in the game."

class ActorNotOnBoardException(ActorException):
    """
    A piece that has not been placed on the board cannot move, scan, capture or be captured
    """
    ERROR_CODE = "ACTOR_NOT_ON_BOARD_ERROR"
    DEFAULT_MESSAGE = "Actor is not on the board. Piece cannot act"

class ActorPlacementRequiredException(ActorException):
    """Raised when a potential actor has not been placed on the board."""
    ERROR_CODE = "ACTOR_PLACEMENT_REQUIRED_ERROR"
    DEFAULT_MESSAGE = (
        "Required actor has an empty position stack. It as not been placed on the board. Event cannot be executed."
    )


# === ACTOR ACTIVITY EXCEPTIONS ===
class CapturedActorCannotActException(ActorException):
    """
    A captured piece cannot actt.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "Actor has been captured. Captured piece cannot act."

class CapturedActorCannotAttackException(ActorException):
    """
    A captured piece cannot attack.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ATTACK_ERROR"
    DEFAULT_MESSAGE = "Actor has been captured. Captured piece cannot attack."

class CapturedActorCannotMoveException(ActorException):
    """
    A captured piece cannot move.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_MOVE_ERROR"
    DEFAULT_MESSAGE = "A captured actor cannot move to a square."

class CapturedActorCannotScanException(ActorException):
    """
    A captured piece cannot scan.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_SCAN_ERROR"
    DEFAULT_MESSAGE = "A captured actor cannot scan a square."

class CheckMatedKingActivityException(ActorException):
    """
    A checkmated king cannot act. The game should end once a king is checkmated
    """
    ERROR_CODE = "CHECKMATED_KING_ACTIVITY_ERROR"
    DEFAULT_MESSAGE = (
        "A checkmated king cannot do anything. The game ends when a king is checkmated."
    )


# === SUBJECT EXCEPTIONS ===
class SubjectException(PieceException):
    """
    SubjectException classes are raised on a piece acted upon. They are raised on the same errors as ActorException,
    Using SubjectException makes tracing which side of the interaction is raising an err easier.
    """
    ERROR_CODE = "SUBJECT_ERROR"
    DEFAULT_MESSAGE = "A potential enemy piece raised an err"


class InvalidSubjectException(SubjectException, InvalidPieceException):
    """Raised if a required enemy fails validate."""
    ERROR_CODE = "SUBJECT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Required enemy failed validate. Actor cannot fire event onto enemy"


class SubjectNotOnBoardException(SubjectException):
    """Raised when a required enemy is not found on the  board."""
    ERROR_CODE = "SUBJECT_NOT_ON_BOARD_ERROR"
    DEFAULT_MESSAGE = "Required enemy was not found on the board. Actor cannot fire event onto enemy"


class SubjectPlacementRequiredException(SubjectException):
    """Raised when a required enemy has not been placed on the board."""
    ERROR_CODE = "SUBJECT_PLACEMENT_REQUIRED_ERROR"
    DEFAULT_MESSAGE = (
        "Required enemy has an empty position stack. It as not been placed on the board. Actor cannot"
        "fire event onto enemy."
    )
