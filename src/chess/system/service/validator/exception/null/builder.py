# src/chess/system/service/validator/exception/null/builder.py

"""
Module: chess.system.service.validator.exception.null.builder
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# ENTITY_SERVICE_NULL_BUILDER EXCEPTION #======================#
    "EntityServiceNullBuilderException",
]

from chess.system import NullException, ServiceException


# ======================# ENTITY_SERVICE_NULL_BUILDER EXCEPTION #======================#
class EntityServiceNullBuilderException(ServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because its builder was null.

    # PARENT:
        *   NullException
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENTITY_SERVICE_NULL_BUILDER_ERROR"
    DEFAULT_MESSAGE = "EntityService validation failed: The candidate's builder was null."