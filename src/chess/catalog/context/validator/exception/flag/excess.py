# src/chess/catalog/validator/exception/flag/excess.py

"""
Module: chess.catalog.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.catalog import InvalidCatalogContextException

__all__ = [
    # ========================= EXCESSIVE_CATALOG_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCatalogContextFlagsException"
]


# ========================= EXCESSIVE_CATALOG_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCatalogContextFlagsException(InvalidCatalogContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one CatalogContext flag was enabled. Only one Catalog attribute-value tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_CATALOG_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive CatalogContext flags were set. Only one CatalogContext flag is allowed."
