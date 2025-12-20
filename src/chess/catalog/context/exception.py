# src/chess/catalog/context/exception.py

"""
Module: chess.catalog.context.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextException
from chess.catalog import CatalogException

__all__ = [
    # ======================# CATALOG_CONTEXT EXCEPTION #======================#
    "CatalogContextException",
]


# ======================# CATALOG_CONTEXT EXCEPTION #======================#
class CatalogContextException(CatalogException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CatalogContext objects.
    2.  Catchall for conditions which are not covered by lower level CatalogContext exceptions.

    # PARENT:
        *   CatalogException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "CatalogContext raised an exception."