# src/chess/catalog/service/exception.py

"""
Module: chess.catalog.service.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# CATALOG_SERVICE EXCEPTION #======================#
    "CatalogServiceException",
]

from chess.catalog import CatalogException
from chess.system import ServiceException


# ======================# CATALOG_SERVICE EXCEPTION #======================#
class CatalogServiceException(CatalogException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an CatalogService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a CatalogService method.

    # PARENT:
        *   ServiceException
        *   CatalogException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CatalogService raised an exception."