# src/chess/team/builder/exception/wrapper.py

"""
Module: chess.team.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-09-02
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# TEAM_BUILD_FAILURE #======================#
    "TeamBuildException",
]


# ======================# TEAM_BUILD_FAILURE #======================#
class TeamBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in TeamBuilder.build that, prevented BuildResult.success() from 
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BUILD_FAILED"
    MSG = "Team build failed."