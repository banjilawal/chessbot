from chess.system import ServiceException
from chess.snapshot import SnapshotException

__all__ = [
    # ======================# SNAPSHOT_SERVICE EXCEPTION #======================#
    "SnapshotServiceException",
]


# ======================# SNAPSHOT_SERVICE EXCEPTION #======================#
class SnapshotServiceException(SnapshotException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an SnapshotService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SnapshotService method.

    # PARENT:
        *   ServiceException
        *   SnapshotException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SnapshotService raised an exception."