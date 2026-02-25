# src/chess/coord/validator/exception/wrapper.py

"""
Module: chess.coord.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# COORD_VALIDATION_FAILURE #======================#
    "CoordValidationException",
]


# ======================# COORD_VALIDATION_FAILURE #======================#
class CoordValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in CoordValidator.validate that, prevented A successful validation result 
        from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "COORD_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Coord validation failed."