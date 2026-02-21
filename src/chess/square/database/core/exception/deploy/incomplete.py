# src/chess/square/database/core/exception/deployment/incomplete.py

"""
Module: chess.square.database.core.exception.deployment.incomplete
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_PARTIALLY_DEPLOYED EXCEPTION #======================#
    "PartialTeamDeploymentException",
]

from chess.square import SquareStackException
from chess.system import DebugException


# ======================# TEAM_PARTIALLY_DEPLOYED EXCEPTION #======================#
class PartialTeamDeploymentException(SquareStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to deploy a team failed because at least one of its members was not 
        placed on the board.

    # PARENT:
        *   SquareStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_PARTIALLY_DEPLOYED_ERROR"
    DEFAULT_MESSAGE = "Deploying team's members failed: At least one member was not placed on the board."