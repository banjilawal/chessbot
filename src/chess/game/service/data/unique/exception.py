# src/chess/game/service/data/unique/exception.py

"""
Module: chess.game.service.data.unique.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    # ======================# UNIQUE_GAME_DATA_SERVICE EXCEPTIONS #======================#
    "UniqueGameDataServiceException",
    "AddingDuplicateGameException",
]


# ======================# UNIQUE_GAME_DATA_SERVICE EXCEPTIONS #======================#
class UniqueGameDataServiceException(DataServiceException):
    """
    Super class of exceptions raised by UniqueGameDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_GAME_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueGameDataService raised an exception."


class AddingDuplicateGameException(UniqueGameDataServiceException):
    """Raised when trying to add a duplicate Game to a list of Games."""
    ERROR_CODE = "DUPLICATE_GAME_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueGameDataService cannot add duplicate Games to the list."