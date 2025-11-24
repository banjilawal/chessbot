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
    "RemovingNullException",
]

class DataServiceException(ServiceException):
    ERROR_CODE = "DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "DataService raised an exception."


class RemovingNullException(DataServiceException):
    ERROR_CODE = "REMOVING_NULL_ERROR"
    DEFAULT_MESSAGE = "Cannot remove an item that does not exist."