# src/model/binder/build/validator.py

"""
Module: model.binder.build.work
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_BUILD_FAILURE #======================#
    "TeamBinderBuildException",
]

from model.team import TeamBinderException
from system import BuildException


# ======================# TEAM_BINDER_BUILD_FAILURE #======================#
class TeamBinderBuildException(TeamBinderException, BuildException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a TeamBinder build failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   TeamException
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_BUILD_FAILURE"
    MSG = "TeamBinder build failed."