# src/chess/edge/validator/exception/wrapper.py

"""
Module: chess.edge.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
Version: 1.0.0
"""

from chess.system import ValidationException

__all__ = [
    # ======================# EDGE_VALIDATION_FAILURE #======================#
    "EdgeValidationException",
]


# ======================# EDGE_VALIDATION_FAILURE #======================#
class EdgeValidationException(ValidationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in EdgeValidator.validate that, prevented A successful validation result 
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
    ERROR_CODE = "EDGE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Edge validation failed."