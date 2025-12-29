# src/chess/token/service/data/unique/exception.py

"""
Module: chess.token.service.data.unique.exception
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import UniqueDataServiceException

__all__ = [
    #======================# UNIQUE_TOKEN_DATA_SERVICE EXCEPTION #======================#
    "UniqueTokenDataServiceException",
    "AddingDuplicateTokenException",
]


#======================# UNIQUE_TOKEN_DATA_SERVICE EXCEPTION #======================#
class UniqueTokenDataServiceException(UniqueDataServiceException):
    """
    Super class of exception raised by UniqueTokenDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_TOKEN_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueTokenDataService raised an exception."


class AddingDuplicateTokenException(UniqueTokenDataServiceException):
    """Raised when trying to add a duplicate Token to a list of Tokens."""
    ERROR_CODE = "DUPLICATE_TOKEN_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueTokenDataService cannot add duplicate Tokens to the list."