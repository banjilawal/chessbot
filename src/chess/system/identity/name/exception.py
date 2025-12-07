# src/chess/system/identity/name/exception.py

"""
Module: chess.system.identity.name.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import BlankTextException, NullException, TextException, ValidationException


__all__ = [
 # ======================# NAME EXCEPTION SUPER CLASS #======================#
    "NameException",
# ======================# NAME VALIDATION EXCEPTIONS #======================#
    "InvalidNameException",
# ======================# NAME NULL/BLANK EXCEPTIONS #======================#
    "NullNameException",
    "WhiteSpaceNameException",
# ======================# NAME LENGTH EXCEPTIONS #======================#
    "ShortNameException",
    "LongNameException",
]


# ======================# NAME EXCEPTION SUPER CLASS #======================#
class NameException(TextException, ValidationException):
    """
    Super class of name exceptions. Subclasses give precise, fine-grained information which make
    debugging faster. Use this exception as a fallback.
    """
    ERROR_CODE = "NAME_ERROR"
    DEFAULT_MESSAGE = "Name raised an exception"


# ======================# NAME VALIDATION EXCEPTIONS #======================#
class InvalidNameException(NameException):
    """
    Super class of name exceptions. Subclasses give precise, fine-grained information which make
    debugging faster. Use this exception as a fallback.
    """
    ERROR_CODE = "NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Name validation failed"


# ======================# NAME NULL/BLANK EXCEPTIONS #======================#
class NullNameException(InvalidNameException, NullException):
    """Raised if an entity, method, or operation requires Name but gets null instead."""
    ERROR_CODE = "NULL_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be null."


class WhiteSpaceNameException(InvalidNameException, BlankTextException):
    """Raised if a name is only white space (" ", "\t", "\n") or, is a blank/empty string ("")"""
    ERROR_CODE = "BLANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be white space only"


# ======================# NAME LENGTH EXCEPTIONS #======================#
class ShortNameException(InvalidNameException):
    """Raised if name is below MIN_NAME_LENGTH."""
    ERROR_CODE = "SHORT_NAME_ERROR"
    DEFAULT_MESSAGE = "The name's length is less MIN_NAME_LENGTH."


class LongNameException(InvalidNameException):
    """Raised if name is above MIN_NAME_LENGTH."""
    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "The name's length is greater than MAX_NAME_LENGTH."
