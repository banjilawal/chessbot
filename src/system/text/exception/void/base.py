# src/logic/system/text/exception/void/anchor.py

"""
Module: logic.system.text.exception.void.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_VOID_STRING EXCEPTION #======================#
    "VoidStringException",
]

from system import InvalidStringException, NullException


#======================# NULL_VOID_STRING EXCEPTION #======================#
class VoidStringException(InvalidStringException):
    """
    Role:Error Tracing, Debugging
    Role:Exception Work
    
    Responsibilities:
    1.  Parent of exceptions which indicate an entity, method, or operation requires a String but gets either
        whitespace, null, or an empty string instead.
    2.  Super for VoidString errors not covered by VoidString subclasses.

    Super Class:
        *   InvalidStringException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_VOID_STRING_EXCEPTION"
    MSG = (
        "Got a String that was either whitespace, null, or an empty string. A String must be contain some characters."
    )