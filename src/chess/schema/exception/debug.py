# src/chess/schema/exception/debug.py

"""
Module: chess.schema.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# SCHEMA_DEBUG EXCEPTION #======================#
    "SchemaDebugException",
]

from chess.schema import SchemaException
from chess.system import DebugException


# ======================# SCHEMA_DEBUG EXCEPTION #======================#
class SchemaDebugException(SchemaException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Schema operation failure.

    # PARENT:
        *   SchemaException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERR_CODE = "SCHEMA_DEBUG_ERROR"
    MSG = "A SchemaDebugException was raised."