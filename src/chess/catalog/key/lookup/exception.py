# src/chess/catalog/lookup/exception.py

"""
Module: chess.catalog.lookup.exception
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
    1.  Wrap an exception that hits the try-finally block of a CatalogLookup method.

    # PARENT:
        *   PersonaException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_LOOKUP_ERROR"
    DEFAULT_MESSAGE = "Persona lookup failed."