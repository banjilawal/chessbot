# src/chess/catalog/validator/exception/base.py

"""
Module: chess.catalog.validator.exception.base
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
    2.  Wrap an exception that hits the try-finally-block in CatalogValidator methods.

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