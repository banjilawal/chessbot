# src/chess/scalar/validator/exception/null.py

"""
Module: chess.scalar.validator.exception.null
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_SCALAR EXCEPTION #======================#
    "NullScalarException",
]

from chess.system import NullException
from chess.scalar import ScalarDebugException


# ======================# NULL_SCALAR EXCEPTION #======================#
class NullScalarException(ScalarDebugException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing ValidationResult was returned because the validation candidate was null.

    # PARENT:
        *   ScalarDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SCALAR_ERROR"
    DEFAULT_MESSAGE = "Scalar validation failed: The validation candidate cannot be null."