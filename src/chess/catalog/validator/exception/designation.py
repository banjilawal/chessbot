# src/chess/catalog/validator/exception/designation.py

"""
Module: chess.catalog.validator.exception.designation
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import InvalidCatalogException
from chess.system import BoundsException, NameException


__all__ = [
    # ======================# CATALOG DESIGNATION BOUNDS EXCEPTIONS #======================#
    "CatalogDesignationBoundsException",
]


# ======================# CATALOG DESIGNATION BOUNDS EXCEPTIONS #======================#
class CatalogDesignationBoundsException(InvalidCatalogException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Catalog designations.

    # PARENT:
        *   InvalidCatalogException
        *   BoundsException
        *   NameException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_DESIGNATION_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Designation is not included in the set of permissible catalog designations."