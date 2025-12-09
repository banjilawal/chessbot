# src/chess/system/err/number.py

"""
Module: chess.system.err.number
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException

__all__ = [
    #======================# NUMBER EXCEPTION SUPER CLASS #======================#
    "NumberException",
    #======================# NUMBER VALIDATION EXCEPTIONS #======================#
    "InvalidNumberException",
    #======================# NULL NUMBER EXCEPTIONS #======================#
    "NullNumberException",
]


#======================# NUMBER EXCEPTION SUPER CLASS #======================#
class NumberException(ChessException):
    """Super class of number related exceptions."""
    ERROR_CODE = "NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number raised an exception."


#======================# NUMBER VALIDATION EXCEPTION #======================#
class InvalidNumberException(NumberException, ValidationException):
    """
    Raised if an entity, method, or operation requires a string with content but gets
    either an empty string or one connecting only white space instead.
    """
    ERROR_CODE = "NUMBER_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Failed number validation."


#======================# NULL/EMPTY STRING EXCEPTIONS #======================#
class NullNumberException(NumberException, NullException):
    """Raised if an entity, method, or operation requires number but gets null instead."""
    ERROR_CODE = "NULL_NUMBER_ERROR"
    DEFAULT_MESSAGE = "Number cannot be null."