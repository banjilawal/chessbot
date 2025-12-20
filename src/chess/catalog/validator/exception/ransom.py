# src/chess/catalog/number_bounds_validator/exception/ransom.py

"""
Module: chess.catalog.number_bounds_validator.exception.ransom
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.catalog import InvalidCatalogException

__all__ = [
    # ======================# CATALOG RANSOM BOUNDS EXCEPTION #======================#
    "CatalogRansomBoundsException",
]


# ======================# CATALOG RANSOM BOUNDS EXCEPTION #======================#
class CatalogRansomBoundsException(InvalidCatalogException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Catalog ransoms.

    # PARENT:
        *   InvalidCatalogException
        *   BoundsException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_RANSOM_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Ransom is not included in the set of permissible catalog ransoms."