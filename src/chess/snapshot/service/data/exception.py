___all__ = [
    # ======================# SNAPSHOT_DATA_SERVICE EXCEPTION #======================#
    "SnapshotDataServiceException",
]

from chess.snapshot import SnapshotException
from chess.system import ServiceException


# ======================# SNAPSHOT_DATA_SERVICE EXCEPTION #======================#
class SnapshotDataServiceException(SnapshotException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SnapshotDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SnapshotDataService method.

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
    ERROR_CODE = "SNAPSHOT_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SnapshotDataService raised an exception."