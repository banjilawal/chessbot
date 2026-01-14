# src/chess/schema/key/service/exception.py

"""
Module: chess.schema.key.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

___all__ = [
    # ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
    "SchemaSuperKeyServiceException",
]

from chess.schema import SchemaSuperKeyException
from chess.system import ServiceException


# ======================# SCHEMA_KEY_SERVICE EXCEPTION #======================#
class SchemaSuperKeyServiceException(SchemaSuperKeyException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaKeyService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaSuperKeyService method.

    # PARENT:
        *   ServiceException
        *   SchemaSuperKeyException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_KEY_SERVICE_ERROR"
    DEFAULT_MESSAGE = "SchemaSuperKeyService raised an exception."