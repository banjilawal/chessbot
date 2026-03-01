# src/logic/team/hash/builder/wrapper.py

"""
Module: logic.team.hash.builder.wrapper
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_BUILD_FAILURE #======================#
    "TeamHashBuildException",
]

from logic.team import TeamHashException
from logic.system import BuildException


# ======================# TEAM_HASH_BUILD_FAILURE #======================#
class TeamHashBuildException(TeamHashException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a TeamHash build failed. The exception chain
        traces the ultimate source of failure.

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
    ERR_CODE = "TEAM_HASH_BUILD_FAILURE"
    MSG = "TeamHash build failed."