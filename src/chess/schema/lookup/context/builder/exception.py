# src/chess/team/schema/context/builder/exception.py

"""
Module: chess.team.schema.context.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.team import SchemaContextException


__all__ = [
    #======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
    "SchemaContextBuildFailedException",
]


#======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
class SchemaContextBuildFailedException(SchemaContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during SchemaContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an SchemaContextBuilder method.
    
    # PARENT:
        *   SchemaContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "SchemaContext build failed."