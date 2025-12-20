# src/chess/catalog/number_bounds_validator/exception/base.py

"""
Module: chess.catalog.number_bounds_validator.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import CatalogException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# CATALOG_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidCatalogException",
]


# ======================# CATALOG VALIDATION EXCEPTION #======================#
class InvalidCatalogException(CatalogException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by CatalogValidation objects.
    2.  Wraps unhandled exceptions that hit the finally-block in CatalogValidator methods.

    # PARENT:
        *   CatalogException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "_CATALOG_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Catalog validation failed."