# src/model/binder/assembly/validator.py

"""
Module: model.binder.assembly.work
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_ASSEMBLY_FAILURE #======================#
    "TeamBinderAssemblyException",
]

from model.state.team import TeamBinderException
from system import AssemblyException


# ======================# TEAM_BINDER_ASSEMBLY_FAILURE #======================#
class TeamBinderAssemblyException(TeamBinderException, AssemblyException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a TeamBinder assembly failed. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   TeamException
        *   AssemblyException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_ASSEMBLY_FAILURE"
    MSG = "TeamBinder assembly failed."