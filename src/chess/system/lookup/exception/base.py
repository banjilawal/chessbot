# src/chess/system/lookup/exception/exception.py

"""
Module: chess.system.lookup.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# LOOKUP EXCEPTION #======================#
    "LookupException",
]


# ======================# LOOKUP EXCEPTION #======================#
class LookupException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Lookup objects
    3.  Catchall for Lookup errors not covered by lower level Lookup exception.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "LOOKUP_ERROR"
    DEFAULT_MESSAGE = "Lookup raised an exception."