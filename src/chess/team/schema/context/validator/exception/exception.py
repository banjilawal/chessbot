# src/chess/team/schema/context/validator/exception/exception.py

"""
Module: chess.team.schema.validator.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.team import TeamSchemaContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# TEAM_SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidTeamSchemaContextException",
]




# ======================# TEAM_SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidTeamSchemaContextException(TeamSchemaContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised TeamSchemaContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in TeamSchemaContextValidator methods.

    # PARENT:
        *   TeamSchemaContextException
        *   ValidationFailedException

    # PROVIDES:
        *   InvalidTeamSchemaContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSchemaContext validation failed."