# src/chess/system/identity/designation/exception.py

"""
Module: chess.system.identity.designation.exception
Author: Banji Lawal
Created: 2025-09-17
version: 1.0.0
"""

from chess.system import BlankTextException, NullException, TextException, ValidationException


__all__ = [
 #======================# NAME EXCEPTION #======================#
    "NameException",
#======================# NAME VALIDATION EXCEPTION #======================#
    "InvalidNameException",
#======================# NAME NULL/BLANK EXCEPTION #======================#
    "NullNameException",
    "WhiteSpaceNameException",
#======================# NAME LENGTH EXCEPTION #======================#
    "ShortNameException",
    "LongNameException",
]


#======================# NAME EXCEPTION #======================#
class NameException(TextException, ValidationException):
    """
    Super class of designation exception. Subclasses give precise, fine-grained information which make
    debugging faster. Use this exception as a fallback.
    """
    ERROR_CODE = "NAME_ERROR"
    DEFAULT_MESSAGE = "Name raised an exception"


#======================# NAME VALIDATION EXCEPTION #======================#
class InvalidNameException(NameException):
    """
    Super class of designation exception. Subclasses give precise, fine-grained information which make
    debugging faster. Use this exception as a fallback.
    """
    ERROR_CODE = "NAME_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Name validation failed"


#======================# NAME NULL/BLANK EXCEPTION #======================#
class NullNameException(InvalidNameException, NullException):
    """Raised if an entity, method, or operation requires Name but gets null instead."""
    ERROR_CODE = "NULL_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be null."


class WhiteSpaceNameException(InvalidNameException, BlankTextException):
    """Raised if a designation is only white space (" ", "\t", "\n") or, is a blank/empty string ("")"""
    ERROR_CODE = "BLANK_NAME_ERROR"
    DEFAULT_MESSAGE = "Name cannot be white space only"


#======================# NAME LENGTH EXCEPTION #======================#
class ShortNameException(InvalidNameException):
    """Raised if designation is below MIN_NAME_LENGTH."""
    ERROR_CODE = "SHORT_NAME_ERROR"
    DEFAULT_MESSAGE = "The designation's length is less MIN_NAME_LENGTH."


class LongNameException(InvalidNameException):
    """Raised if designation is above MIN_NAME_LENGTH."""
    ERROR_CODE = "LONG_NAME_ERROR"
    DEFAULT_MESSAGE = "The designation's length is greater than MAX_NAME_LENGTH."
