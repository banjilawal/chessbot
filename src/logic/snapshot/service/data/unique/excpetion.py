___all__ = [
    # ======================# UNIQUESNAPSHOT_STACK_SERVICE EXCEPTION #======================#
    "UniqueSnapshotDataServiceException",
]

from logic.snapshot import SnapshotException
from logic.system import ServiceException


# ======================# UNIQUE_SNAPSHOT_STACK_SERVICE EXCEPTION #======================#
class UniqueSnapshotDataServiceException(SnapshotException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueSnapshotDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueSnapshotDataService method.

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
    ERR_CODE = "UNIQUE_SNAPSHOT_SERVICE_EXCEPTION"
    MSG = "UniqueSnapshotDataService raised an exception."