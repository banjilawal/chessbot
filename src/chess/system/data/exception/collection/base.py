# src/chess/system/data/exception/collection/__init__.py

"""
Module: chess.system.data.exception.collection.__init__
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DataException

__all__ = [
    "DataSetException",
]


class DataSetException(DataException):
    ERROR_CODE = "DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset raised an exception."