# src/logic/system/collection/schema/exception/anchor.py

"""
Module: logic.system.collection.schema.exception.base
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""


from logic.system import CollectionException, ServiceException

__all__ = [
    # ====================== STACK_SERVICE EXCEPTION #======================#
    "StackServiceException",
]


# ====================== STACK_SERVICE EXCEPTION #======================#
class StackServiceException(ServiceException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Parent of exception raised by StackServices.
    2.  Wraps an exception that hits the try-finally block of a StackService method.

    Super Class:
        *   ServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "STACK_SERVICE_EXCEPTION"
    MSG = "StackService raised an exception."