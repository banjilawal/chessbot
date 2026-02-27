# src/chess/system/collection/hash/service/exception/super.py

"""
Module: chess.system.collection.hash.service.exception.super
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from chess.system import ServiceException


__all__ = [
    # ======================# HASH_SERVICE EXCEPTION #======================#
    "HashServiceException",
]


# ======================# HASH_SERVICE EXCEPTION #======================#
class HashServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Basic, AbstractService Primitive

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HASH_SERVICE_ERROR"
    MSG = "HashService raised an exception."