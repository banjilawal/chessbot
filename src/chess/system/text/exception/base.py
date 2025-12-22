# src/chess/system/text/exception/base.py

"""
Module: chess.system.text.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# STRING EXCEPTION #======================#
    "StringException",

]


#======================# STRING EXCEPTION #======================#
class StringException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised by String objects
    2.  Catchall for String errors not covered by String subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "STRING_ERROR"
    DEFAULT_MESSAGE = "String raised an exception."
