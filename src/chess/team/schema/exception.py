# src/chess/team/schema/exception.py

"""
Module: chess.team.schema.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import BoundsException, NullException, ValidationException

__all__ = [
    #======================# TEAM_SCHEMA EXCEPTION SUPER CLASS #======================#
    "TeamSchemaException",
    
    #======================# TEAM_SCHEMA VALIDATION EXCEPTIONS #======================#
    "InvalidTeamSchemaException",
    "NullTeamSchemaException",
    
    #======================# TEAM_SCHEMA BOUNDS EXCEPTIONS #======================#
    "TeamNameBoundsException",
    "TeamColorBoundsException",
]


#======================# TEAM_SCHEMA EXCEPTION SUPER CLASS #======================#
class TeamSchemaException(TeamException):
    """
    Super class of all exceptions TeamSchema object raises. Do not use directly. Subclasses give
    details useful for debugging.
    """
    ERROR_CODE = "TEAM_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "TeamSchema raised an rexception."


#======================# TEAM_SCHEMA VALIDATION EXCEPTIONS #======================#
class InvalidTeamSchemaException(TeamSchemaException, ValidationException):
    """
    Raised by TeamSchemaValidator if an object fails sanity checks. Exists primarily to catch all
    exceptions raised validating an existingTeamSchema.
    """
    ERROR_CODE = "TEAM_SCHEMA_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSchema validation failed."


class NullTeamSchemaException(TeamSchemaException, NullException):
    """Raised if an entity, method, or operation requires a TeamSchema but gets null."""
    ERROR_CODE = "NULL_TEAM_SCHEMA_ERROR"
    DEFAULT_MESSAGE = "TeamSchema cannot be null."


#======================# TEAM_SCHEMA BOUNDS EXCEPTIONS #======================#
class TeamNameBoundsException(TeamSchemaException, BoundsException):
    """Raised if a name is not in a TeamSchema names"""
    ERROR_CODE = "TEAM_NAME_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Name is not allowed by TeamSchema settings."


class TeamColorBoundsException(TeamSchemaException, BoundsException):
    """Raised if a color is not in a TeamSchema names"""
    ERROR_CODE = "TEAM_COLOR_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "Color is not allowed by TeamSchema settings."
