__all__ = [
    # ======================# RELATION_DEBUG EXCEPTION #======================#
    "RelationDebugException",
]


from chess.system import DebugException, RelationException


# ======================# RELATION_DEBUG EXCEPTION #======================#
class RelationDebugException(RelationException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Relation operation failure.

    # PARENT:
        *   RelationException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "RELATION_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A RelationDebugException was raised."