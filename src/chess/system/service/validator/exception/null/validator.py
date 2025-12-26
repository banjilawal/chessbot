# src/chess/system/service/validator/exception/null/validator.py

"""
Module: chess.system.service.validator.exception.null.validator
Author: Banji Lawal
Created: 2025-11-18
"""

__all__ = [
    # ======================# ENTITY_SERVICE_NULL_VALIDATOR EXCEPTION #======================#
    "EntityServiceNullValidatorException",
]

from chess.system import NullException, ServiceException


# ======================# ENTITY_SERVICE_NULL_VALIDATOR EXCEPTION #======================#
class EntityServiceNullValidatorException(ServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted Service certification because its validator was null.

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
    ERROR_CODE = "ENTITY_SERVICE_NULL_VALIDATOR_ERROR"
    DEFAULT_MESSAGE = "EntityService validation failed: The candidate's validator was null."