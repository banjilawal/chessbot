# src/chess/system/data/exception/remove/exception.py

"""
Module: chess.system.data.exception.remove.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from chess.system.data import DataServiceException


__all__ = ["RemovingNullException"]

class RemovingNullException(DataServiceException):
    ERROR_CODE = "REMOVING_NULL_ERROR"
    DEFAULT_MESSAGE = "Cannot remove an item that does not exist."
    