# src/chess/system/service/validator/exception/null/service.py

"""
Module: chess.system.service.validator.exception.null.service
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# NULL_ENTITY_SERVICE EXCEPTION #======================#
    "NullEntityServiceException",
]

from chess.system import NullException, EntityServiceException


# ======================# NULL_ENTITY_SERVICE EXCEPTION #======================#
class NullEntityServiceException(EntityServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because it was null.

    # PARENT:
        *   NullException
        *   EntityServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ENTITY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "EntityService validation failed: The candidate was null."