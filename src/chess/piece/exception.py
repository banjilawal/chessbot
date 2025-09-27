from chess.exception import ChessException, ValidationException, NullException, BuilderException

__all__ = [
    'PieceException',
    'DoublePromotionException',
    'PieceValidationException',
    'PieceBuilderException',
    'EncounterBuilderException',
    'AlreadyAtDestinationException',
    'NullCoordStackException',
    'CoordStackValidationException',
    'PrisonerEscapeException',
    'PrisonerReleaseException',
    'NullPieceBuilderException',
    'AutoEncounterException',
    'NullPieceException',
    'NullEncounterException',
    'NullKingPieceException',
]

"""
Super class for Piece exceptions
"""
class PieceException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """
    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an team_exception"


class PieceBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when PieceBuilder runs.
    """
    ERROR_CODE = "PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "PieceBuilder raised an exception"


class EncounterBuilderException(BuilderException):
    """
    Wrapper for exceptions raised when EncounterBuilder runs.
    """
    ERROR_CODE = "ENCOUNTER_BUILDER_ERROR"
    DEFAULT_MESSAGE = "EncounterBuilder raised an exception"


class NullPieceBuilderException(NullException):
    """
    Raised if a CoordBuilder is null.
    """
    ERROR_CODE = "NULL_PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "EncounterBuilder cannot be null"


class AutoEncounterException(PieceException):
    ERROR_CODE = "AUTO_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = "Piece cannot encounter itself"


class DoublePromotionException(PieceException):
    """
    If a discovery with validation in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess discovery.
    """
    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again"


class AlreadyAtDestinationException(PieceException):
    """
    If a discovery's destination is its current position raise AlreadyAtDestination.
    """
    ERROR_CODE = "ALREADY_AT_DESTINATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already at the destination."


class PieceValidationException(ValidationException):
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Piece validation failed"


class NullCoordStackException(NullException):
    """
    Raised if a discovery's CoordStack (Piece.positions) is null.
    """
    ERROR_CODE = "NULL_COORD_STACK_ERROR"
    DEFAULT_MESSAGE = f"CoordStack cannot be null"


class CoordStackValidationException(ValidationException):
    ERROR_CODE = "COORDINATE_STACK_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"CoordinateStack validation failed"


class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured hostage raises PrisonerEscapeException. This only applies to hostage pieces
    """
    ERROR_CODE = "MOVING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "A captured discovery cannot be moved on the board"


class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_piece.captor != null to combatant_piece.captor = None
    """
    ERROR_CODE = "RELEASING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor to null once it has been set to an enemy discovery"


# === NULL PIECE RELATED EXCEPTIONS ===
class NullPieceException(NullException):
    """
    Raised if a discovery is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """
    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


class NullEncounterException(NullException):
    """
    NullEncounterException is raised when attempts to put null into a discovery's
    encounter records.
    """
    ERROR_CODE = "NULL_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = f"Encounter cannot be null"


class NullKingPieceException(NullPieceException):
    """
    Raised if a KingPiece is null. Raise NullCombatant instead of NullPieceException
    """
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = f"KingPiece cannot be null"





