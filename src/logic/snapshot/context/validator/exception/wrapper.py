# src/logic/snapshot/validator/exception/base.py

"""
Module: logic.snapshot.validator.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from logic.snapshot import SnapshotContextException
from logic.system import ValidationException

__all__ = [
    # ======================# SNAPSHOT_CONTEXT_VALIDATION_FAILURE #======================#
    "SnapshotContextValidationException",
]


# ======================# SNAPSHOT_CONTEXT_VALIDATION_FAILURE #======================#
class SnapshotContextValidationException(SnapshotContextException, ValidationException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a SnapshotContext. The
        encapsulated exceptions create a chain for tracing the source of the failure.

    Super Class:
        *   SnapshotContextException
        *   ValidationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SNAPSHOT_CONTEXT_VALIDATION_FAILURE"
    MSG = "SnapshotContext validation failed."