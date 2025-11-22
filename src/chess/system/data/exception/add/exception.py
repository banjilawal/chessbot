# src/chess/system/data/exception/add/exception.py

"""
Module: chess.system.data.exception.add.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system.data import DataServiceException


__all__ = ["AddingDuplicateException"]

class AddingDuplicateException(DataServiceException):
    ERROR_CODE = "ADD_DUPLICATE_ITEM_ERROR"
    DEFAULT_MESSAGE = "The item already exists. Adding a duplicate item is not allowed."