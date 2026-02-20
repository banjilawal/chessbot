# src/chess/edge/validator/exception/wrapper.py

"""
Module: chess.edge.validator.exception.wrapper
Author: Banji Lawal
Created: 2026-02-17
"""

from chess.edge import EdgeException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# EDGE_VALIDATION_FAILURE EXCEPTION #======================#
    "EdgeValidationFailedException",
]


# ======================# EDGE_VALIDATION_FAILURE EXCEPTION #======================#
class EdgeValidationFailedException(EdgeException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Edge. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   EdgeException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EDGE_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "Edge validation failed."