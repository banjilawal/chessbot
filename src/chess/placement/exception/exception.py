# src/chess/layout/exception/base.py

"""
Module: chess.layout.exception.base.py
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system.err import ChessException

__all__  = [
    "LayoutException",
]




class LayoutException(ChessException):
    """"""
    ERROR_CODE = "LAYOUT_ERROR"
    DEFAULT_MESSAGE = "Layout raised an exception."