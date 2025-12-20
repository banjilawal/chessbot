# src/chess/catalog/number_bounds_validator/exception/null.py

"""
Module: chess.catalog.number_bounds_validator.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import NullException
from chess.catalog import InvalidCatalogException


__all__ = [
    # ======================# NULL CATALOG EXCEPTION #======================#
    "NullCatalogException",
]


# ======================# NULL CATALOG EXCEPTION #======================#
class NullCatalogException(InvalidCatalogException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an Catalog validation candidate is null.
    2.  Raised if an entity, method or operation requires an Catalog but receives null instead.

    # PARENT:
        *   InvalidCatalogException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_ORDER_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "Catalog cannot be null."
