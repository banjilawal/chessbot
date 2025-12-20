# src/chess/catalog/service/exception.py

"""
Module: chess.catalog.service.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import Catalog
from chess.system import ServiceException

__all__ = [
    # ======================# CATALOG_SERVICE EXCEPTION #======================#
    "CatalogServiceException",
]


# ======================# CATALOG_SERVICE EXCEPTION #======================#
class CatalogServiceException(Catalog, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an CatalogService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting CatalogService's
        processes from their normal flows.

    # PARENT:
        *   Catalog
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_SERVICE_ERROR"
    DEFAULT_MESSAGE = "CatalogService raised an exception."

