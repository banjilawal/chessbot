from chess.exception import  ValidationException, NullException
from chess.operation import OperationExecutorException

__all__ = [
    'OccupationException',
    'InvalidOccupationDirectiveException',
    'NullOccupationDirectiveException',
    'AutoOccupationException',
    'HostageValidationException',
    'NullHostagePieceException',
    'InvalidOccupationDirectiveException',
    'OccupationSearchException',
]

class OccupationException(OperationExecutorException):
    ERROR_CODE = "OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "An exception was raised while executing the square occupation"

class AutoOccupationException(OccupationException):
    ERROR_CODE = "AUTO_OCCUPATION_ERROR"
    DEFAULT_MESSAGE = "You are already occupying the square"


class NullOccupationDirectiveException(NullException):
    ERROR_CODE = "NULL_OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "OccupationDirective cannot be null"


class InvalidOccupationDirectiveException(ValidationException):
    """OccupationDirective validation failure."""

    ERROR_CODE = "OCCUPATION_DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "OccupationDirective failed validation"


class HostageValidationException(OccupationException):
    ERROR_CODE = "HOSTAGE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Hostage validation failed"


class NullHostagePieceException(OccupationException):
    """
    Raised if a subject is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """

    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


class NullCombatantPieceException(OccupationException):
    """
    Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = f"CombatantPiece cannot be null"


class OccupationSearchException(OccupationException):
    """
    Board searches during an occupation should not fai. If they do there is an inconsistency in the board
    """

    ERROR_CODE = "OCCUPATION_SEARCH_ERROR"
    DEFAULT_MESSAGE = f"BoardSearch failed to find a square; this should not happen in an occupation operation"