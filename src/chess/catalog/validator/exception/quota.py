# src/chess/catalog/validator/exception/quota.py

"""
Module: chess.catalog.validator.exception.quota
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import BoundsException
from chess.catalog import InvalidCatalogException


__all__ = [
    # ======================# CATALOG QUOTA BOUNDS EXCEPTIONS #======================#
    "CatalogQuotaBoundsException",
]


# ======================# CATALOG QUOTA BOUNDS EXCEPTIONS #======================#
class CatalogQuotaBoundsException(InvalidCatalogException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate an error occurred because a designation is outside the range of acceptable Catalog quotas.

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
    ERROR_CODE = "CATALOG_QUOTA_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Quota is not included in the set of permissible catalog quotas."