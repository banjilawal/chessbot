# src/chess/edge/context/validator/exception/wrapper.py

"""
Module: chess.edge.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

from chess.system import ValidationException
from chess.edge import EdgeContextException

__all__ = [
    # ======================# EDGE_CONTEXT_VALIDATION_FAILURE #======================#
    "EdgeContextValidationException",
]


# ======================# EDGE_CONTEXT_VALIDATION_FAILURE #======================#
class EdgeContextValidationException(EdgeContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a EdgeContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   EdgeContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "EdgeContext validation failed."