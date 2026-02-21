# src/chess/system/text/exception/void/base.py

"""
Module: chess.system.text.exception.void.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_VOID_STRING EXCEPTION #======================#
    "VoidStringException",
]

from chess.system import InvalidStringException, NullException


#======================# NULL_VOID_STRING EXCEPTION #======================#
class VoidStringException(InvalidStringException):
    """
    # ROLE: Error Tracing, Debugging
    # ROLE: Exception Wrapper
    
    # RESPONSIBILITIES:
    1.  Parent of exceptions which indicate an entity, method, or operation requires a String but gets either
        whitespace, null, or an empty string instead.
    2.  Catchall for VoidString errors not covered by VoidString subclasses.

    # PARENT:
        *   InvalidStringException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_VOID_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that was either whitespace, null, or an empty string. A String must be contain some characters."
    )