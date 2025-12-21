# src/chess/system/data/exception/collection/_null.py

"""
Module: chess.system.data.exception.collection._null
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DataSetException, NullException

__all__ = [
    "NullDataSetException",
]


class NullDataSetException(DataSetException, NullException):
    ERROR_CODE = "NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "Dataset cannot be null."