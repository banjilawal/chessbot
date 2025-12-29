# src/chess/team/builder/exception/wrapper.py

"""
Module: chess.team.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import BuildFailedException


__all__ = [
    # ======================# TEAM_BUILD_FAILED EXCEPTION #======================#
    "TeamBuildFailedException",
]


# ======================# TEAM_BUILD_FAILED EXCEPTION #======================#
class TeamBuildFailedException(TeamException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Team build creates an exception. Failed check exceptions are encapsulated
        in an TeamBuildFailedException which is sent to the caller in a BuildResult.
    2.  The TeamBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   TeamException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_BUILD_FAILED"
    DEFAULT_MESSAGE = "Team build failed."