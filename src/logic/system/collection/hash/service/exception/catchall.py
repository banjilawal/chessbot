# src/logic/system/collection/hash/service/exception/super.py

"""
Module: logic.system.collection.hash.service.exception.super
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from logic.system import ServiceException


__all__ = [
    # ======================# HASH_SERVICE EXCEPTION #======================#
    "HashServiceException",
]


# ======================# HASH_SERVICE EXCEPTION #======================#
class HashServiceException(ServiceException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Basic, Service Primitive

    Super Class:
        *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "HASH_SERVICE_EXCEPTION"
    MSG = "HashService raised an exception."