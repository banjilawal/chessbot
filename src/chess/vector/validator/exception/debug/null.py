# src/chess/vector/validator/exception/null.py

"""
Module: chess.vector.validator.exception.null
Author: Banji Lawal
Created: 2025-08-12
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_VECTOR EXCEPTION #======================#
    "NullVectorException",
]

from chess.system import NullException
from chess.vector import VectorDebugException


# ======================# NULL_VECTOR EXCEPTION #======================#
class NullVectorException(VectorDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the candidate was null.

    # PARENT:
        *   VectorDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_VECTOR_ERROR"
    MSG = "Vector validation failed: The candidate cannot be null."