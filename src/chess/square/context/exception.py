# src/chess/square/context/exception.py

"""
Module: chess.square.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.square import SquareException
from chess.system import ContextException

__all__ = [
    # ======================# SQUARE_CONTEXT EXCEPTION #======================#
    "SquareContextException",
]


# ======================# SQUARE_CONTEXT EXCEPTION #======================#
class SquareContextException(ContextException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareService.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SquareService raised an exception."
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for SquareContext errors not covered by SquareException subclasses.

    # PARENT:
        *   SquareException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "SQUARE_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "SquareContext raised an exception."
    