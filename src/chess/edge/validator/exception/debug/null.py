# src/chess/edge/validator/exception/null.py

"""
Module: chess.edge.validator.exception.null
Author: Banji Lawal
Created: 2026-02-18
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_EDGE EXCEPTION #======================#
    "NullEdgeException",
]

from chess.system import NullException
from chess.edge import EdgeDebugException


# ======================# NULL_EDGE EXCEPTION #======================#
class NullEdgeException(EdgeDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   EdgeDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_EDGE_ERROR"
    MSG = "Edge validation failed: The candidate cannot be null."