# src/chess/system/text/exception/void/blank.py

"""
Module: chess.system.text.exception.void.blank
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import VoidStringException

__all__ = [
    # ======================# BLANK_EMPTY_STRING EXCEPTION #======================#
    "BlankEmptyStringException",
]




#======================# BLANK_EMPTY_STRING EXCEPTION #======================#
class BlankEmptyStringException(VoidStringException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Parent of exceptions which indicate an entity, method, or operation got a String with no characters and no
        whitespace.
    2.  Catchall for errors not covered by BlankEmptyString subclasses.

    # PARENT:
        *   VoidStringException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BLANK_EMPTY_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a blank String that had no characters nor whites space. The String cannot be empty it must have "
        "some characters."
    )