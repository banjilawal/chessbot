# src/chess/system/text/exception/void/null.py

"""
Module: chess.system.text.exception.void.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_STRING EXCEPTION #======================#
    "NullStringException",
]

from chess.system import NullException, VoidStringException


#======================# NULL_STRING EXCEPTION #======================#
class NullStringException(VoidStringException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an entity, method, or operation required a String with some characters but got null instead.

    # PARENT:
        *   VoidStringException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_STRING_ERROR"
    DEFAULT_MESSAGE = "String cannot be null. A String must be contain some characters."