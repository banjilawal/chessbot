__all__ = [
    # ======================# ATTACKING_DISABLED_ENEMY EXCEPTION #======================#
    "AttackingDisabledEnemyException",
]

from logic.attack import AttackDebugException


# ======================# ATTACKING_DISABLED_ENEMY EXCEPTION #======================#
class AttackingDisabledEnemyException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the was already disabled.

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
    MSG = "Attack failed: The enemy combatant was already disabled."