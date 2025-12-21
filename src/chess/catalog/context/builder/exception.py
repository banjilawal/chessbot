# src/chess/catalog/map/builder/exception.py

"""
Module: chess.catalog.map.builder.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.catalog import CatalogContextException


__all__ = [
    # ======================# CATALOG_CONTEXT BUILD EXCEPTION #======================#
    "CatalogContextBuildFailedException",
]


# ======================# CATALOG_CONTEXT BUILD EXCEPTION #======================#
class CatalogContextBuildFailedException(CatalogContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during CatalogContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an CatalogContextBuilder method.

    # PARENT:
        *   CatalogContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CATALOG_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "CatalogContext build failed."