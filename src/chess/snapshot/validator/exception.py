__all__ = [
    # ======================# SNAPSHOT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSnapshotException",
]

from chess.snapshot import SnapshotException


# ======================# SNAPSHOT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSnapshotException(SnapshotException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a Snapshot candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidSnapshotException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidSnapshotException chain is useful for tracing a  failure to its source.

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