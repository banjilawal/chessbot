# src/chess/team/builder/exception.py

"""
Module: chess.team.builder.exception
Author: Banji Lawal
Created: 2025-09-04
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
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Any failed check during the TeamContext build creates an exception. Failed check exceptions are encapsulated
        in an TeamContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The TeamContextBuildFailedException provides a trace for debugging and application recovery.tion recovery.

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
    ERROR_CODE = "TEAM_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Team build failed."