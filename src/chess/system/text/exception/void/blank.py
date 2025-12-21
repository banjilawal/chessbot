# src/chess/system/text/exception/void/blank.py

"""
Module: chess.system.text.exception.void.blank
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


__all__ = [
    # ======================# BLANK_EMPTY_STRING EXCEPTION #======================#
    "BlankEmptyStringException",
]


#======================# BLANK_EMPTY_STRING EXCEPTION #======================#
class BlankEmptyStringException(VoidStringException):
    """Raised if an entity, method, or operation requires a String but gets either whitespace, null, or an empty string instead.her null or an empty string"""
    ERROR_CODE = "BLANK_EMPTY_STRING_ERROR"
    DEFAULT_MESSAGE = (
        "Got a String that was either whitespace, null, or an empty string. A String must be non-null and non-empty."
    )