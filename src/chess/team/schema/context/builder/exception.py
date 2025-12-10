# src/chess/teamSchema/context/builder/exception.py

"""
Module: chess.teamSchema.context.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.teamSchema import TeamSchemaContextException


__all__ = [
    #======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
    "TeamSchemaContextBuildFailedException",
]


#======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
class TeamSchemaContextBuildFailedException(TeamSchemaContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during TeamSchemaContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamSchemaContextBuilder method.
    
    # PARENT
        *   TeamSchemaContextException
        *   BuildFailedException

    # PROVIDES:
        *   TeamSchemaContextBuildFailedException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "TeamSchemaContext build failed."