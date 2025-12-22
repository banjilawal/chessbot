from chess.system import ServiceException
from chess.snapshot import SnapshotContextException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_SERVICE EXCEPTION #======================#
    "SnapshotContextServiceException",
]


# ======================# SNAPSHOT_CONTEXT_SERVICE EXCEPTION #======================#
class SnapshotContextServiceException(SnapshotContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SnapshotContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an SnapshotContextService method.

    # PARENT:
        *   ServiceException
        *   SnapshotContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SnapshotContextService raised an exception."