# src/chess/system/data/service/stack/unique/exception.py

"""
Module: chess.system.data.service.stack.unique.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system.data import StackServiceException

__all__ = [
    "UniqueStackServiceException",
]

class UniqueStackServiceException(StackServiceException):
    ERROR_CODE = "UNIQUE_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueStackService raised an exception."