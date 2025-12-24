# src/chess/coord/validator/exception/exception.py

"""
Module: chess.coord.validator.exception.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.coord import CoordContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# COORD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "InvalidCoordContextException",
]


# ======================# COORD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class InvalidCoordContextException(CoordContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  A debug exception is created when a CoordContext candidate fails a validation test. Validation debug exceptions are
        encapsulated inside an InvalidCoordContextException creating an exception chain. which is sent to the caller in a
        ValidationResult.
    2.  The InvalidCoordContextException chain is useful for tracing a  failure to its source.

    # PARENT:
        *   CoordContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "CoordContext validation failed."