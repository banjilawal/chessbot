# src/chess/team/builder/base.py

"""
Module: chess.team.builder.exception
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import BuildFailedException


__all__ = [
    # ======================# TEAM BUILD EXCEPTIONS #======================#
    "TeamBuildFailedException",
]


# ======================# TEAM BUILD EXCEPTIONS #======================#
class TeamBuildFailedException(TeamException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by TeamBuilder 
    prevents successful Team creation.
    """
    ERROR_CODE = "TEAM_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Team build failed."