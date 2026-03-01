# src/logic/schema/key/service/exception.py

"""
Module: logic.schema.key.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

___all__ = [
    # ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
    "SchemaKeyServiceException",
]

from logic.schema import SchemaKeyException
from logic.system import ServiceException


# ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
class SchemaKeyServiceException(SchemaKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaKeyService method.

    # PARENT:
        *   ServiceException
        *   SchemaKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_KEY_SERVICE_EXCEPTION"
    MSG = "SchemaKeyService raised an exception."