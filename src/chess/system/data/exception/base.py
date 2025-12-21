# src/chess/system/data/exception/base.py

"""
Module: chess.system.data.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "DataException",
]

class DataException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Data owned by a DataService
    3.  Catchall for errorss not covered by lower level DataException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DATA_ERROR"
    DEFAULT_MESSAGE = "A piece of data managed by a DataService has encountered an error."