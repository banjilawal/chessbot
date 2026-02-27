__all__ = [
    # ======================# ATTACKING_ENEMY_KING EXCEPTION #======================#
    "AttackingEnemyKingException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKING_ENEMY_KING EXCEPTION #======================#
class AttackingEnemyKingException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the enemy was a king.

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The enemy was a king which can only be checked or checkmated."