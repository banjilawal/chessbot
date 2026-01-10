__all__ = [
    # ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
    "PushingCoordFailedException",
]

from chess.coord import CoordDataServiceException
from chess.system import OperationFailedException


# ======================# PUSHING_COORD_ONTO_STACK_FAILURE EXCEPTION #======================#
class PushingCoordFailedException(CoordDataServiceException, OperationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why pushing a Coord onto the stack fails. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   CoordDataServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PUSHING_COORD_ONTO_STACK_FAILURE"
    DEFAULT_MESSAGE = "Pushing a Coord onto the stack failed."