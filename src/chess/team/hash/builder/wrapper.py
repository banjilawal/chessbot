# src/chess/team/hash/builder/wrapper.py

"""
Module: chess.team.hash.builder.wrapper
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_BUILD_FAILURE EXCEPTION #======================#
    "TeamHashBuildFailedException",
]

from chess.team import TeamHashException
from chess.system import BuildFailedException


# ======================# TEAM_HASH_BUILD_FAILURE EXCEPTION #======================#
class TeamHashBuildFailedException(TeamHashException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a TeamHash build failed. The exception chain
        traces the ultimate source of failure.

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
    ERROR_CODE = "TEAM_HASH_BUILD_FAILURE"
    DEFAULT_MESSAGE = "TeamHash build failed."