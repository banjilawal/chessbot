__all__ = [
    # ======================# UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
    "SnapshotContextValidationRouteException",
]

from chess.snapshot import SnapshotException
from chess.system import UnhandledRouteException


# ======================# UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE EXCEPTION #======================#
class SnapshotContextValidationRouteException(SnapshotException, UnhandledRouteException):
    """
    # ROLE: Fallback Result, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the SnapshotContext validation failed because there was no build route for the SnapshotContext key.

    # PARENT:
        *   ResultException
        *   UnhandledRouteException

    # PROVIDES
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "UNHANDLED_SNAPSHOT_CONTEXT_VALIDATION_ROUTE_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext validation failed: No validation route was provided for the Snapshot attribute."