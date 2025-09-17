from chess.exception import ChessException, ValidationException, NullException, NameValidationException

"""
Super class for Piece exceptions
"""
class PieceException(ChessException):
    """
    Super class for exceptions raised by Piece objects
    """

    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an team_exception"



class DoublePromotionException(PieceException):
    """
    If a piece with validation in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess piece.
    """

    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again"


class AlreadyAtDestinationException(PieceException):
    """
    If a piece's destination is its current position raise AlreadyAtDestination.
    """

    ERROR_CODE = "ALREADY_AT_DESTINATION_ERROR"
    DEFAULT_MESSAGE = "Piece is already at the destination."


class PieceValidationException(ValidationException):
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Piece validation failed"


class PieceCoordNullException(PieceException):
    """
    PieceCoordNullException gets thrown if a piece with an empty coord stack attempts to move.
    If piece.positions.is_empty == True then the piece is not on the board so it cannot be moved.
    """

    ERROR_CODE = "PIECE_NO_COORDINATE_ERROR"
    DEFAULT_MESSAGE = "Piece is not on the board. Cannot move a piece with len(piece.positions) == 0"

class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured hostage raises PrisonerEscapeException. This only applies to hostage pieces
    """

    ERROR_CODE = "MOVING_CAPTURED_PIECE_ERROR"


class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_piece.captor != null to combatant_piece.captor = None
    """

    ERROR_CODE = "RELEASING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor to null once it has been set to an enemy piece"

# === NULL PIECE RELATED EXCEPTIONS ===

class NullPieceException(NullException):
    """
    Raised if a piece is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """

    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


class NullCombatantPieceException(NullPieceException):
    """
    Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = f"CombatantPiece cannot be null"


class NullEncounterException(NullException):
    """
    NullEncounterException is raised when attempts to put null into a piece's
    encounter records.
    """

    ERROR_CODE = "NULL_ENCOUNTER_ERROR"
    DEFAULT_MESSAGE = f"Encounter cannot be null"


class NullHostagePieceException(NullPieceException):
    """
    Raised if a piece is null. Parent class for:
        - NullCombatantPieceException
        - NullKingException
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Use a finegrained subclass of NullPieceException.
    """

    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = f"Piece cannot be null"


class NullKingPieceException(NullPieceException):
    """
    Raised if a KingPiece is null. Raise NullCombatant instead of NullPieceException
    """

    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = f"KingPiece cannot be null"





