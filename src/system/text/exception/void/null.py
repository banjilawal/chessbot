# src/logic/system/text/exception/void/null.py

"""
Module: logic.system.text.exception.void.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_STRING EXCEPTION #======================#
    "NullStringException",
]

from system import NullException, VoidStringException


#======================# NULL_STRING EXCEPTION #======================#
class NullStringException(VoidStringException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate an entity, method, or operation required a String with some characters but got null instead.

    Super Class:
        *   VoidStringException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_STRING_EXCEPTION"
    MSG = "String cannot be null. A String must be contain some characters."