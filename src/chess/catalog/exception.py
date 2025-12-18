# src/chess/catalog/exception.py

"""
Module: chess.catalog.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "CatalogException",
]


class CatalogException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Catalog objects.
    2.  Catchall for conditions which are not covered by lower level Catalog exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_ERROR"
    DEFAULT_MESSAGE = "Catalog raised an exception."
