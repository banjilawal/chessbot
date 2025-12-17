# src/chess/team/schema/validator/exception/base.py

"""
Module: chess.team.schema.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.team import TeamSchemaException
from chess.system import ValidationFailedException


__all__ = [
    #======================# TEAM_SCHEMA_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidTeamSchemaException",
]

#======================# TEAM_SCHEMA VALIDATION SUPER CLASS #======================#
class InvalidTeamSchemaException(TeamSchemaException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised TeamSchema validation.
    2.  Wraps unhandled exceptions that hit the finally-block in TeamSchemaValidator methods.
    
    # PARENT:
        *   TeamSchemaException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSchema validation failed."
