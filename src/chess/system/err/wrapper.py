# src/chess/system/err/wrapper.py

"""
Module: chess.system.err.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# NOT_IMPLEMENTED EXCEPTION #======================#
    "ExceptionWrapper",
]

from chess.system import ChessException


# ======================# WRAPPER EXCEPTION #======================#
class ExceptionWrapper(ChessException):
    """
    # ROLE: Wrapper, Encapsulation, Messaging

    # RESPONSIBILITIES:
    1.  Wraps exceptions creating an exception chain. Unwrapping the chain gives the source of an error.
    2.  Are the desired exception type in a Result.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "EXCEPTION_WRAPPER"
    DEFAULT_MESSAGE = "ExceptionWrapper"