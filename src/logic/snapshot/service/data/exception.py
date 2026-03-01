___all__ = [
    # ======================# SNAPSHOT_STACK_SERVICE EXCEPTION #======================#
    "SnapshotDataServiceException",
]

from logic.snapshot import SnapshotException
from logic.system import ServiceException


# ======================# SNAPSHOT_STACK_SERVICE EXCEPTION #======================#
class SnapshotDataServiceException(SnapshotException, ServiceException):
    """
    # ROLE: Exception Wrapper

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
    ERR_CODE = "SNAPSHOT_STACK_EXCEPTION"
    MSG = "SnapshotDataService raised an exception."