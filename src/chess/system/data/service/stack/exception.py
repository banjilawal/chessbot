# src/chess/system/data/service/stack/exception.py

"""
Module: chess.system.data.service.stack.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system.data import DataServiceException

__all__ = ["StackServiceException"]


class StackServiceException(DataServiceException):
    ERROR_CODE = "STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "StacKService raised an exception."