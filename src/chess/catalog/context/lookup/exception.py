# src/chess/catalog/lookup/exception/failure.py

"""
Module: chess.catalog.lookup.exception.failure
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import OperationFailedException
from chess.catalog import CatalogLookupException

__all__ = [
    # ======================# CATALOG_LOOKUP_FAILED EXCEPTION #======================#
    "CatalogLookupFailedException",
]


# ======================# CATALOG_LOOKUP_FAILED EXCEPTION #======================#
class CatalogLookupFailedException(CatalogLookupException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Wraps unhandled exceptions that hit the try-finally block of a CatalogLookup.look method.

    # PARENT:
        *   CatalogLookupException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "Catalog lookup failed."