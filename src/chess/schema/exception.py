# src/chess/schema/exception.py

"""
Module: chess.schema.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    # ======================# SCHEMA_SCHEMA EXCEPTION #======================#
    "SchemaException",
]


# ======================# SCHEMA EXCEPTION #======================#
class SchemaException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by Schema objects.
    2.  Catchall for conditions which are not covered by lower level Schema exceptions.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMA_SCHEMA_ERROR"
    DEFAULT_ERROR_CODE = "Schema raised an exception."
