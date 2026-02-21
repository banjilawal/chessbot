# src/chess/coord/context/validator/wrapper.py

"""
Module: chess.coord.context.validator.wrapper
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.coord import CoordContextException
from chess.system import ValidationException

__all__ = [
    # ======================# COORD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "CoordContextValidationException",
]


# ======================# COORD_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class CoordContextValidationException(CoordContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a CoordContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   CoordContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "CoordContext validation failed."