# src/chess/catalog/validator/exception/name.py

"""
Module: chess.catalog.validator.exception.name
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import InvalidCatalogException
from chess.system import BoundsException, NameException

__all__ = [
    # ======================# CATALOG NAME BOUNDS EXCEPTION #======================#
    "CatalogNameBoundsException",
]


# ======================# CATALOG NAME BOUNDS EXCEPTION #======================#
class CatalogNameBoundsException(InvalidCatalogException, BoundsException, NameException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a name is outside the range of acceptable Persona names.

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
    ERROR_CODE = "CATALOG_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not included in the set of permissible catalog names."