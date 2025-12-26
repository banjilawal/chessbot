# src/chess/system/err/catchall.py

"""
Module: chess.system.err.catchall
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# CATCHALL EXCEPTION #======================#
    "CatchallException",
]

from chess.system import ChessException


# ======================# CATCHALL EXCEPTION #======================#
class CatchallException(ChessException):
    """
    # ROLE: Wrapper, Catchall

    # RESPONSIBILITIES:
    1.  Parent of a collection of debug and wrapper exceptions for an entity objects that support it
    2.  Raised when subclasses do not provide coverage for an error case.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "CATCHALL_ERROR"
    DEFAULT_MESSAGE = "CatchallException"