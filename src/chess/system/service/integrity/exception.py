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
    # ROLE: Exception Wrapper
    
    # A AbstractService bundles methods that return different classes of Result.

    # RESPONSIBILITIES:
    1.  Parent of exception raised by AbstractService objects
    2.  Super for AbstractService errors not covered by lower level AbstractService exception.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ENTITY_SERVICE_ERROR"
    MSG = "IntegrityService raised an exception."
