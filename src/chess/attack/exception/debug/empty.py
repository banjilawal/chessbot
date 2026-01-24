__all__ = [
    # ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
    "AttackingVacantSquareException",
]


# ======================# ATTACKING_EMPTY_SQUARE EXCEPTION #======================#
class AttackingVacantSquareException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because there was nothing in the square.

    # PARENT:
        *   AttackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACKING_EMPTY_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Attack failed: The square was empty. There was nothing to attack."