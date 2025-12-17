# src/chess/team/schema/lookup/context/exception.py

"""
Module: chess.team.schema.lookup.context.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ContextException
from chess.team import TeamSchemaException

__all__ = [
    # ======================# SCHEMA_CONTEXT EXCEPTION SUPER CLASS #======================#
    "SchemaContextException",
]



# ======================# SCHEMA_CONTEXT EXCEPTION SUPER CLASS #======================#
class SchemaContextException(TeamSchemaException, ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by SchemaContext objects.
    2.  Catchall for conditions which are not covered by lower level SchemaContext exceptions.

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
    ERROR_CODE = "SCHEMA_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "SchemaContext raised an exception."