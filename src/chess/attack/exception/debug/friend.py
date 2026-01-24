__all__ = [
    # ======================# ATTACKING_FRIENDLY_SQUARE EXCEPTION #======================#
    "AttackingFriendlySquareException",
]


# ======================# ATTACKING_FRIENDLY_SQUARE EXCEPTION #======================#
class AttackingFriendlySquareException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because the square was occupied by a friend.
    
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
    DEFAULT_MESSAGE = "Attack failed: The square was occupied by a friend."