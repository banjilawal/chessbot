from chess.exception import ChessException, ValidationException, NullException, BuilderException, RollbackException

__all__ = [
    'PieceException',
    'PieceRollBackException',

# === PIECE VALIDATION EXCEPTIONS ===
    'InvalidPieceException',
    'UnregisteredTeamMemberException',

# === NULL PIECE EXCEPTIONS ===
    'NullPieceException',
    'NullKingException',
    'NullCombatantException',

# === PIECE BUILD EXCEPTIONS ===
    'PieceBuildFailedException',

# === PIECE PROMOTION EXCEPTIONS ===
    'DoublePromotionException',
    'DoublePromotionRolledBackException',

# === PIECE CAPTURE EXCEPTIONS ===
    'CapturePieceException',
    'CaptureFriendException',
    'KingCaptureException',
    'DoubleCaptureException',
    'UnsetCaptureException',

# === PIECE CAPTURE EXCEPTIONS WITH ROLLBACK ===
    'RollBackCaptureException',
    'CaptureFriendRolledBackException',
    'KingCaptureRolledBackException',
    'DoubleCaptureRolledBackException',
    'UnsetCaptureRolledBackException',

# === ATTACKING PIECE EXCEPTIONS ===
    'HostageActivityException',
    'HostageCannotAttackException',
    'HostageCannotMoveException',
    'HostageCannotScanException'
]

class PieceException(ChessException):
    """
    Super class of all exceptions a Piece object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all piece exceptions
    """
    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an exception."

class PieceRollBackException(PieceException, RollbackException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "PIECE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Piece raised an exception."


# === PIECE VALIDATION EXCEPTIONS ===
class InvalidPieceException(PieceException, ValidationException):
    """Raised by PieceValidators if client fails validation."""
    ERROR_CODE = "PIECE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Piece validate failed."

class UnregisteredTeamMemberException(PieceException):
    """Raised if a piece has its team set but the piece is not on the roster"""
    ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "The piece has team but is not listed on the roster."


# === NULL PIECE EXCEPTIONS ===
class NullPieceException(PieceException, NullException):
    """
    Raised if an entity, method, or operation requires a piece but gets null instead.
    Piece is an abstract method. KingPiece and CombatantPiece are its subclasses.
    Do not throw NullPieceException. Raise NullKingPiece or NullCombatantPiece instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece cannot be null."

class NullKingException(NullPieceException):
    """
    Raised if a KingPiece is null. Raise NullCombatant instead of NullPieceException
    """
    ERROR_CODE = "NULL_KING_PIECE_ERROR"
    DEFAULT_MESSAGE = "KingPiece cannot be null."

class NullCombatantException(NullPieceException):
    """
    Raised if a CombatantPiece is null. Raise NullCombatant instead of NullPieceException
    """
    ERROR_CODE = "NULL_COMBATANT_PIECE_ERROR"
    DEFAULT_MESSAGE = "CombatantPiece cannot be null."


# === PIECE BUILD EXCEPTIONS ===
class PieceBuildFailedException(PieceException, BuilderException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Piece  build failed.."


# === PIECE PROMOTION EXCEPTIONS ===
class DoublePromotionException(PieceException):
    """
    Raised when attempting promoting a piece already elevated to Queen rank.
    Only pieces with Pawn or King rank can be promoted.
    """
    ERROR_CODE = "DOUBLE_PROMOTION_ERROR"
    DEFAULT_MESSAGE = "Piece is already promoted to Queen. It cannot be promoted again."

class DoublePromotionRolledBackException(PieceRollBackException):
    """
    Raised if a transaction attempts promoting a piece already elevated to Queen rank.
    Only pieces with Pawn or King rank can be promoted.  The transaction was rolled
    back before raising this err.
    """
    ERROR_CODE = "DOUBLE_PROMOTION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Piece is already promoted to Queen. It cannot be promoted again. Transaction "
        "rollback performed."
    )


# === PIECE CAPTURE EXCEPTIONS ===
class CapturePieceException(PieceException):
    """
    Several exceptions can be raised during capture operations. This class is the parent of
    exceptions a piece can raise being captured or attacking. Do not use directly. Subclasses
    give details useful for debugging.
    """
    ERROR_CODE = "PIECE_CAPTURE_ERROR"
    DEFAULT_MESSAGE = "Piece capture attempt raised and err"

class CaptureFriendException(CapturePieceException):
    """
    Raised if a piece attempts to capture a friend.
    """
    ERROR_CODE = "FRIEND_CAPTURE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a friend."

class KingCaptureException(CapturePieceException):
    """
    Raised if a piece attempts to capture an enemy king. Kings can only be checked or
    checkmated.
    """
    ERROR_CODE = "KING_CAPTURE_ERROR"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be captured. It can only be checked or checkmated."
    )

class DoubleCaptureException(CapturePieceException):
    """
    Raised when a piece attempts to capture an enemy combatant that is already a prisoner
    """
    ERROR_CODE = "DOUBLE_CAPTURE_ERROR"
    DEFAULT_MESSAGE = "Cannot capture a piece that is already a prisoner."

class UnsetCaptureException(CapturePieceException):
    """
    If piece.captor is not null. Attempting to change it raises this err
    """
    ERROR_CODE = "UNSET_CAPTOR_ERROR"
    DEFAULT_MESSAGE =(
        "Cannot set a prisoner's captor to null. A captured piece cannot be freed."
    )


class CircularCaptureException(CapturePieceException):
    """
    Raised if a piece tries to capture itself.
    """
    ERROR_CODE = "CIRCULAR_CAPTURE_ERROR"
    DEFAULT_MESSAGE = "Piece cannot capture itself"


# === PIECE CAPTURE EXCEPTIONS WITH ROLLBACK ===
class RollBackCaptureException(CapturePieceException, RollbackException):
    """
    RollBackCapture exceptions should be raised in ACID transactions where a capture can
    raise an err. Do not use directly. Subclasses give details useful for debugging.
    """
    ERROR_CODE = "CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Capture raised an exception. Transaction rolled back."

class CaptureFriendRolledBackException(RollBackCaptureException):
    """
    Raised if a transaction attempts capturing a friend. The transaction
    was rolled back before raising this err.
    """
    ERROR_CODE = "FRIEND_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot capture a friend. Transaction rollback performed."
    )

class KingCaptureRolledBackException(RollBackCaptureException):
    """
    Raised if a transaction attempts capturing an enemy. Kings can only be checked or
    checkmated. The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "KING_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "An enemy king cannot be captured. It can only be checked or checkmated. "
        "Transaction rollback performed."
    )

class DoubleCaptureRolledBackException(RollBackCaptureException):
    """
    Raised if a transaction attempts capturing an enemy combatant that is already
    a prisoner. The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "DOUBLE_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot capture a piece that is already a prisoner. Transaction "
        "rollback performed."
    )

class UnsetCaptureRolledBackException(RollBackCaptureException):
    """
    Raised if a transaction attempts setting prisoner's captor field null.
    The transaction was rolled back before raising this err.
    """
    ERROR_CODE = "UNSET_CAPTOR_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Cannot set a prisoner's captor to null. A captured piece cannot be freed. "
        "Transaction rollback performed."
    )


class CircularCaptureRolledBackException(CapturePieceException):
    """
    Raised if a transaction attempts to set a piece as its own captor. The transaction was
    rolled back before raising this err.
    """
    ERROR_CODE = "CIRCULAR_CAPTURE_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Piece cannot capture itself. Transaction rolled back."


# === ATTACKING PIECE EXCEPTIONS ===
class HostageActivityException(PieceException):
    """
    Several exceptions can be raised during capture operations. This class is the parent of
    exceptions an attacking piece can raised. Do not use directly. Subclasses give details
    useful for debugging.
    """
    ERROR_CODE = "HOSTAGE_ACTIVITY_ERROR"
    DEFAULT_MESSAGE = "Hostage piece cannot move, scan, or attack."


class HostageCannotAttackException(HostageActivityException):
    """
    Raised if a captured piece tries to attack.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_ATTACK_ERROR"
    DEFAULT_MESSAGE = "Captured piece cannot attack."

class HostageCannotMoveException(HostageActivityException):
    """
    Raised if a captured piece tries to move.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_MOVE_ERROR"
    DEFAULT_MESSAGE = "Captured piece cannot move."

class HostageCannotScanException(HostageActivityException):
    """
    Raised if a captured piece tries to scan a square.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_SCAN_ERROR"
    DEFAULT_MESSAGE = "Captured piece cannot scan a sqaure."


