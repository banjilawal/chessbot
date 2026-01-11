__all__ = [
    # ======================# SNAPSHOT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSnapshotException",
]

from chess.snapshot import SnapshotException
from chess.system import ValidationFailedException


# ======================# SNAPSHOT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSnapshotException(SnapshotException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why a candidate failed its validation as a Snapshot. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   SnapshotException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Snapshot validation failed."