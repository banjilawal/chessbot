# src/chess/snapshot/context/validator/exception/base.py

"""
Module: chess.snapshot.context.validator.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.game import SnapshotContextException
from chess.system import ValidationFailedException


__all__ = [
    # ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidSnapshotContextException",
]


# ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidSnapshotContextException(SnapshotContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised SnapshotContext validation.
    2.  Wraps unhandled exception that hit the finally-block in SnapshotContextValidator methods.

    # PARENT:
        *   SnapshotContextException
        *   ValidationFailedException

    # PROVIDES:
    InvalidSnapshotContextException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "SnapshotContext validation failed."