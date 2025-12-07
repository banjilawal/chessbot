# src/chess/system/data/result/base.py

"""
Module: chess.system.data.result.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ResultException


class EmptyDataResultException(ResultException):
    """DataResult must contain either a payload or an exception"""
    ERROR_CODE = "EMPTY_DATA_RESULT_ERROR"
    DEFAULT_MESSAGE = "DataResult must contain either a payload or an exception. It cannot be empty."