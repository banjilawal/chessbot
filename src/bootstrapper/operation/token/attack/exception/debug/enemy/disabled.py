__all__ = [
    # ======================# ATTACKING_DISABLED_ENEMY EXCEPTION #======================#
    "AttackingDisabledEnemyException",
]

from operation.microservice.token import AttackDebugException


# ======================# ATTACKING_DISABLED_ENEMY EXCEPTION #======================#
class AttackingDisabledEnemyException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate an attack failed because the was already disabled.

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The enemy combatant was already disabled."