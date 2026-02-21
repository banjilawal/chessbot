# src/chess/square/database/core/exception/deployment/wrapper.py

"""
Module: chess.square.database.core.exception.deployment.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_ROSTER_DEPLOYMENT_FAILURE #======================#
    "DeployingTeamRosterException",
]

from chess.square import SquareStackException
from chess.system import UpdateFailedException


# ======================# TEAM_ROSTER_DEPLOYMENT_FAILURE #======================#
class DeployingTeamRosterException(SquareStackException, UpdateFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that deploying all the team's members to their opening squares failed.

    # PARENT:
        *   SquareStackException
        *   UpdateFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_ROSTER_DEPLOYMENT_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Deploying team's members failed."