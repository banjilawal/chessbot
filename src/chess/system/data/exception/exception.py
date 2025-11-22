# src/chess/system/data/exception/exception.py

"""
Module: chess.system.data.exception.__init__
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ChessException

__all__ = ["DataServiceException"]

class DataServiceException(ChessException):
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "DataService raised an exception."