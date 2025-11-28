# src/chess/system/err/text.py

"""
Module: chess.system.err.text
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
# ======================# TEXT EXCEPTION SUPER CLASS #======================#
    "TextException",

# ======================# NULL STRING EXCEPTIONS #======================#
    "NullStringException",

# ======================# BLANK/WHITE SPACE STRING EXCEPTIONS #======================#
    "BlankStringException",
]

# ======================# TEXT EXCEPTION SUPER CLASS #======================#
class TextException(ChessException):
    """Super class of text related exceptions."""
    ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
    DEFAULT_MESSAGE = "Cannot old_search by validation string"


# ======================# NULL/EMPTY STRING EXCEPTIONS #======================#
class NullStringException(TextException, NullException):
    """Raised if an entity, method, or operation requires string but gets null instead."""
    ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
    DEFAULT_MESSAGE = "Cannot old_search by validation string"


# ======================# BLANK/WHITE SPACE STRING EXCEPTIONS #======================#
class BlankStringException(TextException):
    """
    Raised if an entity, method, or operation requires a string with content but gets
    either an empty string or one conating only white space instead.
    """
    ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
    DEFAULT_MESSAGE = "Cannot old_search by an empty or blank string"