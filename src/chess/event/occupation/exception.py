from chess.exception import  ValidationException, NullException
from chess.transaction import EventException

__all__ = [
    'OccupationEventException',
    'InvalidOccupationEventException',
    'NullOccupationEventException',
    'CircularOccupationException',
    'HostageValidationEventException',
    'NullHostagePieceEventException',
    'InvalidOccupationEventException',
    'OccupationSearchEventException',
]

class OccupationEventException(EventException):
    ERROR_CODE = "OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "An exception was raised while executing the square occupation"

class CircularOccupationException(OccupationEventException):
    ERROR_CODE = "CIRCULAR_OCCUPATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already occupying the destination square"


class NullOccupationEventException(NullException):
    ERROR_CODE = "NULL_OCCUPATION_EXECUTION_ERROR"
    DEFAULT_MESSAGE = "OccupationDirective cannot be null"


class InvalidOccupationEventException(ValidationException):
    """OccupationDirective validation failure."""

    ERROR_CODE = "OCCUPATION_DIRECTIVE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "OccupationDirective failed validation"


class HostageValidationEventException(OccupationEventException):
    ERROR_CODE = "HOSTAGE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Hostage validation failed"


class NullHostagePieceEventException(OccupationEventException):
    """
    Raised if a subject is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """

    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


class NullCombatantPieceEventException(OccupationEventException):
    """
    Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = f"CombatantPiece cannot be null"


class OccupationSearchEventException(OccupationEventException):
    """
    Board searches during an occupation should not fai. If they do there is an inconsistency in the board
    """

    ERROR_CODE = "OCCUPATION_SEARCH_ERROR"
    DEFAULT_MESSAGE = f"BoardSearch failed to find a square; this should not happen in an occupation operation"