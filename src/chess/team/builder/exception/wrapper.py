# src/chess/team/builder/exception/wrapper.py

"""
Module: chess.team.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import BuildException


__all__ = [
    # ======================# TEAM_BUILD_FAILURE EXCEPTION #======================#
    "TeamBuildException",
]


# ======================# TEAM_BUILD_FAILURE EXCEPTION #======================#
class TeamBuildException(TeamException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Team build creates an exception. Failed check exceptions are encapsulated
        in an TeamBuildException which is sent to the caller in a BuildResult.
    2.  The TeamBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   TeamException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_BUILD_FAILED"
    DEFAULT_MESSAGE = "Team build failed."