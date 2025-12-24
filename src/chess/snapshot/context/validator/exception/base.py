# src/chess/snapshot/validator/exception/base.py

"""
Module: chess.snapshot.validator.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""



from chess.system import ValidationFailedException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSnapshotContextException",
]


# ======================# SNAPSHOT_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSnapshotContextException(SnapshotContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a SnapshotContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidSnapshotContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidSnapshotContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   SnapshotContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SnapshotContext validation failed."