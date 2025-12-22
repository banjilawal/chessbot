# src/chess/catalog/map/validator/exception/flag/zero.py

"""
Module: chess.catalog.map.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.catalog import InvalidCatalogContextException

__all__ = [
    # ========================= ZERO_CATALOG_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroCatalogContextFlagsException"
]


# ========================= ZERO_CATALOG_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroCatalogContextFlagsException(InvalidCatalogContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  no CatalogContext flag was enabled. One and only one Catalog attribute-value tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidCatalogContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_CATALOG_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero CatalogContext flags were set. One and only one map flag must be enabled,"
