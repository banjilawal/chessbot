# src/logic/schema/service/exception.py

"""
Module: logic.schema.service.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.system import ServiceException
from logic.schema import SchemaException

__all__ = [
    # ======================# SCHEMA_SERVICE EXCEPTION #======================#
    "SchemaServiceException",
]


# ======================# SCHEMA_SERVICE EXCEPTION #======================#
class SchemaServiceException(SchemaException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that an SchemaService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a SchemaService method.

    # PARENT:
        *   ServiceException
        *   SchemaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_SERVICE_EXCEPTION"
    MSG = "SchemaService raised an exception."