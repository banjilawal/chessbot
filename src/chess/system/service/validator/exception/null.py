# src/chess/system/service/validator/exception/null.py

"""
Module: chess.system.service.validator.exception.null
Author: Banji Lawal
Created: 2025-11-18
"""

from chess.system import InvalidServiceException, NullException

__all__ = [
    # ======================# NULL_SERVICE EXCEPTION #======================#
    "NullServiceException",
]


#======================# NULL_SERVICE EXCEPTION #======================#
class NullServiceException(InvalidServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an entity, method or operation requires an Service but receives null instead.

    # PARENT:
        *   NullServiceException
        *   InvalidServiceException

    # PROVIDES:

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_SERVICE_ERROR"
    DEFAULT_MESSAGE = "Service cannot be null."
