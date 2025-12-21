# src/chess/catalog/map/validator/exception/null.py

"""
Module: chess.catalog.map.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from chess.system import NullException
from chess.catalog import InvalidCatalogContextException

__all__ = [
    # ======================# CATALOG_CONTEXT NULL EXCEPTION #======================#
    "NullCatalogContextException",
]


# ======================# CATALOG_CONTEXT NULL EXCEPTION #======================#
class NullCatalogContextException(InvalidCatalogContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an CatalogContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an CatalogContext but receives null instead.

    # PARENT:
        *   InvalidCatalogContextException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_CATALOG_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CatalogContext cannot be null."