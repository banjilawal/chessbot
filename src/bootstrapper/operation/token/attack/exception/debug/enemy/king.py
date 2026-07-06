__all__ = [
    # ======================# ATTACKING_ENEMY_KING EXCEPTION #======================#
    "AttackingEnemyKingException",
]

from operation.token.attack import AttackDebugException


# ======================# ATTACKING_ENEMY_KING EXCEPTION #======================#
class AttackingEnemyKingException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attack failed because the enemy was a king.

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The enemy was a king which can only be check or checkmated."