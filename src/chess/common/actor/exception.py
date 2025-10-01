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

# === PIECE BUILDER EXCEPTIONS ===
    'PieceBuilderException',

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
    'AttackerException',
    'PrisonerCannotAttackException'
]

class ActorException(PieceException):
    """
    Super class of all exceptions an actor object can raise. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all piece exceptions
    """
    ERROR_CODE = "ACTOR_ERROR"
    DEFAULT_MESSAGE = "Actor raised an exception"

class ActorRollBackException(ActorException, RollbackException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "ACTOR_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = "Actor raised an exception. Transaction rolled back"


class ActorNotOnBoardException(ActorException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "ACTOR_NOT_ON_BOARD_ERROR"
    DEFAULT_MESSAGE = "Actor is not on the board. Piece cannot act"

class CapturedActorCannotAttackException(ActorException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_ATTACK_ERROR"
    DEFAULT_MESSAGE = "Actor has been captured. Captured piece cannot attack."

class CapturedActorCannotMoveException(ActorException):
    """
    Any inconsistencies a piece introduces into a transaction need to be rolled back.
    This is the super class of a piece mutator operations, methods, or fields that raise
    errors. Do not use directly. Subclasses give details useful for debugging. This class
    exists primarily to allow catching all Piece exceptions that happen when a failed
    transaction must be rolled back.
    """
    ERROR_CODE = "CAPTURED_ACTOR_CANNOT_MOVE_ERROR"
    DEFAULT_MESSAGE = "A captured actor cannot move to a square."