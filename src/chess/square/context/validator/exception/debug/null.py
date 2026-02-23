# src/chess/square/context/validator/exception/debug/null.py

"""
Module: chess.square.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.system import NullException
from chess.square import SquareContextException

__all__ = [
    # ======================# NULL_SQUARE_CONTEXT EXCEPTION #======================#
    "NullSquareContextException",
]


# ======================# NULL_SQUARE_CONTEXT EXCEPTION #======================#
class NullSquareContextException(SquareContextException, NullException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
        1.  A failing ValidationResult was returned because the candidate was null

    # PARENT:
        *   SquareContextDebugException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext validation failed: The candidate was null."