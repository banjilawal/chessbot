# src/chess/catalog/validator/exception/flag/zero.py

"""
Module: chess.catalog.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.catalog import InvalidPersonaSuperKeyException


__all__ = [
    # ========================= ZERO_CATALOG_CONTEXT_ENUM_TUPLES EXCEPTION =========================#
    "ZeroPersonaSuperKeyEnumTuplesException",
]


# ========================= ZERO_CATALOG_CONTEXT_ENUM_TUPLES EXCEPTION =========================#
class ZeroPersonaSuperKeyEnumTuplesException(InvalidPersonaSuperKeyException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no CatalogContext flag is provided for a forward Persona lookup.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidPersonaSuperKeyException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_CATALOG_CONTEXT_ENUM_TUPLES_ERROR"
    DEFAULT_MESSAGE = (
        "No CatalogContext flag was selected. A CatalogContext must be enabled with an attribute-value-tuple"
        " to perform a forward Persona entry lookup."
    )