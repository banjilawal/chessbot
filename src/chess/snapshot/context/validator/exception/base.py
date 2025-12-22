# src/chess/snapshot/map/validator/exception/base.py

"""
Module: chess.snapshot.map.validator.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""



from chess.system import ValidationFailedException


__all__ = [
    # ======================# SNAPSHOT_CONTEX_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidSnapshotContextException",
]


# ======================# SNAPSHOT_CONTEX_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidSnapshotContextException(SnapshotContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a candidate failed SnapshotContext validation checks.
    2.  Wraps unhandled exception that hit the try-finally block of a SnapShotContextValidator method.
    3.  Catchall for validation errors not handled by InvalidSnapshotContextException subclasses.

    # PARENT:
        *   SnapshotContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SNAPSHOT_CONTEX_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "SnapshotContext validation failed."