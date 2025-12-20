# src/chess/catalog/lookup/context/number_bounds_validator/exception/flag.py

"""
Module: chess.catalog.lookup.context.exception.flag
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.catalog import InvalidCatalogContextException

__all__ = [
    # ========================= NO_CATALOG_CONTEXT_FLAG EXCEPTION =========================#
    "NoCatalogContextFlagException",
    # ========================= TOO_MANY_CATALOG_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveCatalogContextFlagsException"
]


# ========================= NO_CATALOG_CONTEXT_FLAG EXCEPTION =========================#
class NoCatalogContextFlagException(InvalidCatalogContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no CatalogContext flag is provided for a Catalog lookup.

    # PARENT:
        *   InvalidCatalogContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_CATALOG_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No CatalogContext flag was selected. A context flag must be turned on with a target value."


# ========================= TOO_MANY_CATALOG_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveCatalogContextFlagsException(InvalidCatalogContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, CatalogContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Catalog attribute is going to be used in a Catalog lookup.

    # PARENT:
        *   InvalidCatalogContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_CATALOG_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one CatalogContext flag was selected. Only one context flag is allowed."
