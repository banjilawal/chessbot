# src/chess/team/context/builder/exception/wrapper.py

"""
Module: chess.team.context.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamContextException
from chess.system import BuildFailedException


__all__ = [
    # ======================# TEAM_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
    "TeamContextBuildFailedException",
]


# ======================# TEAM_CONTEXT_BUILD_FAILURE EXCEPTION #======================#
class TeamContextBuildFailedException(TeamContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the TeamContext build creates an exception. Failed check exceptions are encapsulated
        in an TeamContextBuildFailedException which is sent to the caller in a BuildResult.
    2.  The TeamContextBuildFailedException provides a trace for debugging and application recovery.

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
    ERROR_CODE = "TEAM_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "TeamContext build failed."