AttackingVacantSquareException

__all__ = [
    # ======================# ATTACKING_TOKEN_ON_WRONG_BOARD EXCEPTION #======================#
    "AttackingTokenOnWrongBoardException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKING_TOKEN_ON_WRONG_BOARD EXCEPTION #======================#
class AttackingTokenOnWrongBoardException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the attacker was targeting the wrong board,

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACKING_EMPTY_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Attack failed: The attacked is targeting the wrong board."