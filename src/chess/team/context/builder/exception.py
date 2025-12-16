# src/chess/team/context/builder/exception.py

"""
Module: chess.team.context.builder.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamContextException
from chess.system import BuildFailedException

__all__ = [
    #======================# TEAM_CONTEXT BUILD EXCEPTIONS #======================#
    "TeamContextBuildFailedException",
]


# ======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
class TeamContextBuildFailedException(TeamContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during TeamContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamContextBuilder method.

    # PARENT:
        *   TeamContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "TeamContext build failed."