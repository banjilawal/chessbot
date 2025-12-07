# src/chess/system/data/entity_service/unique/base.py

"""
Module: chess.system.data.entity_service.unique.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    "UniqueDataServiceException",
    "AddingDuplicateDataException",
]


class UniqueDataServiceException(DataServiceException):
    ERROR_CODE = "UNIQUE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueDataService raised an exception."


class AddingDuplicateDataException(UniqueDataServiceException):
    ERROR_CODE = "ADDING_DUPLICATE_DATA_ERROR"
    DEFAULT_MESSAGE = "The data already exists. Adding duplicate data is not allowed."