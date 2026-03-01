# src/logic/schema/key/exception.base.py

"""
Module: logic.schema.key.exception.base
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from logic.schema import SchemaException
from logic.system import ContextException


__all__ = [
    # ======================# SCHEMA_KEY EXCEPTION #======================#
    "SchemaKeyException",
]


# ======================# SCHEMA_KEY EXCEPTION #======================#
class SchemaKeyException(SchemaException, ContextException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Super for conditions which are not covered by SchemaKeyException subclasses.

    # PARENT:
        *   SchemaException
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SCHEMA_KEY_EXCEPTION"
    DEFAULT_ERR_CODE = "SchemaKey raised an exception."