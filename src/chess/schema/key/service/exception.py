# src/chess/schema/key/service/exception.py

"""
Module: chess.schema.key.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

___all__ = [
    # ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
    "SchemaKeyServiceException",
]

from chess.schema import SchemaKeyException
from chess.system import ServiceException


# ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
class SchemaKeyServiceException(SchemaKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

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
    ERROR_CODE = "SCHEMA_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SchemaKeyService raised an exception."