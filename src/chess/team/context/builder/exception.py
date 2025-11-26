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
    "TeamContextBuildFailedException",
]




# ======================# TEAM BUILD EXCEPTIONS #======================#
class TeamContextBuildFailedException(TeamContextException, BuildFailedException):
    """Catchall Exception for TeamContextBuilder when it encounters an error building a Team."""
    ERROR_CODE = "TEAM_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamContext build failed."