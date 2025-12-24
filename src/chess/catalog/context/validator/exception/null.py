# src/chess/catalog/validator/exception/null.py

"""
Module: chess.catalog.exception.null
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""


from chess.system import NullException
from chess.catalog import InvalidPersonaSuperKeyException

__all__ = [
    # ======================# CATALOG_CONTEXT NULL EXCEPTION #======================#
    "NullPersonaSuperKeyException",
]


# ======================# CATALOG_CONTEXT NULL EXCEPTION #======================#
class NullPersonaSuperKeyException(InvalidPersonaSuperKeyException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an CatalogContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an CatalogContext but receives null instead.

    # PARENT:
        *   InvalidPersonaSuperKeyException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_CATALOG_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "CatalogContext cannot be null."