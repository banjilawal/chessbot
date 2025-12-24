# src/chess/schema/exception.py

"""
Module: chess.schema.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    # ======================# SCHEMA EXCEPTION #======================#
    "SchemaException",
]


# ======================# SCHEMA EXCEPTION #======================#
class SchemaException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Schema errors not covered by SchemaException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_ERROR"
    DEFAULT_MESSAGE = "Schema raised an exception."