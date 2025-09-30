from chess.exception import ChessException, ValidationException, NullException, BuilderException

__all__ = [
    'PieceException',
    'DoublePromotionException',
    'InvalidPieceException',
    'PieceBuilderException',
    'DoubleCoordPushException',
    'NullCoordStackException',
    'CoordStackValidationException',
    'PrisonerEscapeException',
    'PrisonerReleaseException',
    'NullPieceBuilderException',
    'NullPieceException',
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


class NullPieceBuilderException(PieceException, NullException):
    """
    Raised if a CoordBuilder is null.
    """
    ERROR_CODE = "NULL_PIECE_BUILDER_ERROR"
    DEFAULT_MESSAGE = "DiscoveryBuilder cannot be null"


class UnregisteredTeamMemberException(PieceException):
    """Raised if a piece has its team set but the piece is not on the roster"""
    ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "The piece has team but is not listed on the roster."


class DoublePromotionException(PieceException):
    """
    If a discover with validation in [Pawn, King] has been promoted to Queen, DoublePromotionException
    is raised if there is a second attempt to promote the chess discover.
    """
    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again"





class InvalidPieceException(PieceException, ValidationException):
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = f"Piece validation failed"


class PrisonerEscapeException(PieceException):
    """
    Combatant pieces with attacker field not null cannot be moved. Attempts to move
    a captured hostage raises PrisonerEscapeException. This only applies to hostage pieces
    """
    ERROR_CODE = "MOVING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "A captured discover cannot be moved on the board"


class PrisonerReleaseException(PieceException):
    """
    Combatant.captor field can only be set once. PrisonerReleaseException is thrown when an attempt to change
    combatant_piece.captor != null to combatant_piece.captor = None
    """
    ERROR_CODE = "RELEASING_CAPTURED_PIECE_ERROR"
    DEFAULT_MESSAGE = "Cannot change CombatantPiece.captor to null once it has been set to an enemy discover"


# === NULL PIECE RELATED EXCEPTIONS ===
class NullPieceException(PieceException, NullException):
    """
    Raised if a discover is null. Parent class for:
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





