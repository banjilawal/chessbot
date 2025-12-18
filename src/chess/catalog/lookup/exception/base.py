# src/chess/catalog/lookup/exception/base.py

"""
Module: chess.catalog.lookup.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import CatalogException

__all__ = [
    # ======================# CATALOG_LOOKUP EXCEPTION #======================#
    "CatalogLookupException",
]


# ======================# CATALOG_LOOKUP EXCEPTION #======================#
class CatalogLookupException(CatalogException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CatalogLookup objects.
    2.  Raised when no specific exception exists for the error interrupting CatalogLookup's
        processes from their normal flows.

    # PARENT:
        *   CatalogException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "CatalogLookup raised an exception."