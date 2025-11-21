# src/chess/system/err/null.py

"""
Module: chess.system.err.null
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    "NullException",
    "NullNumberException",
    "NullStringException",
    "BlankStringException",
]

class NullException(ChessException):
    """
    Raised if an entity, method, or operation requires not null but gets null instead.
    """
    ERROR_CODE = "NULL_ERROR"
    DEFAULT_MESSAGE = "cannot be null"


class NullNumberException(NullException):
    """
    Raised if mathematical expression or geometric, algebraic, or optimization that need
     number but get null instead NUllNumberException is thrown. Ids are not used for math
     so we need different null team_exception for math variables
    """
    ERROR_CODE = "NULL_NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number cannot be null"


class NullStringException(NullException):
    """
    Raised if an entity, method, or operation requires string but gets null instead.
    """
    ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
    DEFAULT_MESSAGE = "Cannot old_search by null string"


class BlankStringException(ChessException):
    """
    Raised if old_search parameter is blank or empty string
    """
    ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
    DEFAULT_MESSAGE = "Cannot old_search by an empty or blank string"

