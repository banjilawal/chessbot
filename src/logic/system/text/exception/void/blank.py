# src/logic/system/text/exception/void/blank.py

"""
Module: logic.system.text.exception.void.blank
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from logic.system import VoidStringException

__all__ = [
    # ======================# BLANK_EMPTY_STRING EXCEPTION #======================#
    "BlankEmptyStringException",
]




#======================# BLANK_EMPTY_STRING EXCEPTION #======================#
class BlankEmptyStringException(VoidStringException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Parent of exceptions which indicate an entity, method, or operation got a String with no characters and no
        whitespace.
    2.  Super for errors not covered by BlankEmptyString subclasses.

    Super Class:
        *   VoidStringException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BLANK_EMPTY_STRING_EXCEPTION"
    MSG = (
        "Got a blank String that had no characters nor whites space. The String cannot be empty it must have "
        "some characters."
    )