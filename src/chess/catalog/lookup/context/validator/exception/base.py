# src/chess/catalog/lookup/context/number_bounds_validator/exception/base.py

"""
Module: chess.catalog.lookup.context.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import CatalogContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# CATALOG_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidCatalogContextException",
]


# ======================# CATALOG_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidCatalogContextException(CatalogContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised CatalogContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in CatalogContextValidator methods.

    # PARENT:
        *   CatalogContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "CatalogContext validation failed."