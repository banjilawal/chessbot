# src/chess/team/context/builder/base.py

"""
Module: chess.team.context.builder.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamContextException
from chess.system import BuildFailedException

__all__ = [
    # ======================# TEAM_CONTEXT BUILD EXCEPTIONS #======================#
    "TeamContextBuildFailedException",
]


# ======================# TEAM_CONTEXT BUILD EXCEPTIONS #======================#
class TeamContextBuildFailedException(TeamContextException, BuildFailedException):
    """
    Catchall exception for when TeamContextBuilder encounters an error building a new TeamContext instance.
    """
    ERROR_CODE = "TEAM_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamContext build failed."