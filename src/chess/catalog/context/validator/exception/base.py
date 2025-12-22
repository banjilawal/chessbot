# src/chess/catalog/map/validator/exception/base.py

"""
Module: chess.catalog.map.exception.base
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.catalog import CatalogContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# CATALOG_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidCatalogContextException",
]


# ======================# CATALOG_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidCatalogContextException(CatalogContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised CatalogContext validation.
    2.  Wraps exceptions that hit the try-finally-block in CatalogContextValidator methods.

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