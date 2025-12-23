# src/chess/system/service/entity/exception.py

"""
Module: chess.system.service.entity.exception
Author: Banji Lawal
Created: 2025-11-18
"""


__all__ = [
    # ======================# ENTITY_SERVICE EXCEPTION #======================#
    "EntityServiceException",
]

from chess.system import ServiceException


# ======================# ENTITY_SERVICE EXCEPTION #======================#
class EntityServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # A Service bundles methods that return different classes of Result.

    # RESPONSIBILITIES:
    1.  Parent of exception raised by Service objects
    2.  Catchall for Service errors not covered by lower level Service exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENTITY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "EntityService raised an exception."
