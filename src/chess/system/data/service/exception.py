# src/chess/system/data/service/exception.py

"""
Module: chess.system.data.service.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    "DataServiceException",
    "RemovingNullDataException",
    "PoppingEmptyStackException",
]

class DataServiceException(ServiceException):
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "DataService raised an exception."


class RemovingNullDataException(DataServiceException):
    ERROR_CODE = "REMOVING_NULL_DATA_ERROR"
    DEFAULT_MESSAGE = "Cannot remove data that does not exist."


class PoppingEmptyStackException(DataServiceException):
    ERROR_CODE = "POPPING_EMPTY_STACK_ERROR"
    DEFAULT_MESSAGE = "Stack is empty. There is nothing to poop."