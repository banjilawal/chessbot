__all__ = [
    # ======================# SNAPSHOT_VALIDATION_FAILURE #======================#
    "InvalidSnapshotException",
]

from chess.snapshot import SnapshotException
from chess.system import ValidationException


# ======================# SNAPSHOT_VALIDATION_FAILURE #======================#
class InvalidSnapshotException(SnapshotException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Snapshot. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   SnapshotException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Snapshot validation failed."