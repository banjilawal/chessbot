# src/chess/system/err/text/exception.py

"""
Module: chess.system.err.text.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException

__all__ = [
# ======================# TEXT EXCEPTION SUPER CLASS #======================#
    "TextException",
# ======================# INVALID TEXT EXCEPTIONS #======================#
    "InvalidTextException",
# ======================# NULL TEXT EXCEPTIONS #======================#
    "NullTextException",
# ======================# BLANK/WHITE SPACE TEXT EXCEPTIONS #======================#
    "BlankTextException",
]


# ======================# TEXT EXCEPTION SUPER CLASS #======================#
class TextException(ChessException):
    """Super class of text related exceptions."""
    ERROR_CODE = "TEXT_ERROR"
    DEFAULT_MESSAGE = "Text raised an exception."


# ======================# INVALID TEXT EXCEPTIONS #======================#
class InvalidTextException(TextException, ValidationException):
    """Raised if TextValidator candidate fails a check."""
    ERROR_CODE = "TEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Failed text validation."


# ======================# NULL/EMPTY TEXT EXCEPTIONS #======================#
class NullTextException(InvalidTextException, NullException):
    """Raised if an entity, method, or operation requires text but gets null instead."""
    ERROR_CODE = "NULL_TEXT_ERROR"
    DEFAULT_MESSAGE = "Text cannot be null."


# ======================# BLANK/WHITE SPACE TEXT EXCEPTIONS #======================#
class BlankTextException(InvalidTextException):
    """Raised if a text is empty or white space only."""
    ERROR_CODE = "BLANK_TEXT_ERROR"
    DEFAULT_MESSAGE = "Text cannot be white space only nor empty."