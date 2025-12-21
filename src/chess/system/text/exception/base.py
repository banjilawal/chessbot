# src/chess/system/text/exception/base.py

"""
Module: chess.system.text.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# STRING EXCEPTION #======================#
    "StringException",

]


#======================# STRING EXCEPTION #======================#
class StringException(ChessException):
    """Super class of text related exception."""
    ERROR_CODE = "STRING_ERROR"
    DEFAULT_MESSAGE = "String raised an exception."
