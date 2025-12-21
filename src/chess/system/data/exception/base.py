# src/chess/system/data/exception/base.py

"""
Module: chess.system.data.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "DataException",
]

class DataException(ChessException):
    ERROR_CODE = "DATA_ERROR"
    DEFAULT_MESSAGE = "Data exception was raised."