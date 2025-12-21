# src/chess/system/data/exception/base.py

"""
Module: chess.system.data..exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
    "DataException",
    "DataSetException",
    "NullDataSetException",
]

class DataException(ChessException):
    ERROR_CODE = "DATA_ERROR"
    DEFAULT_MESSAGE = "Data exception was raised."



class DataSetException(ChessException):
    ERROR_CODE = "DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset raised an exception."


class NullDataSetException(DataSetException, NullException):
    ERROR_CODE = "NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset cannot be null."