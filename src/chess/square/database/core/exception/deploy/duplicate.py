# src/chess/square/database/core/exception/deployment/duplicate.py

"""
Module: chess.square.database.core.exception.deployment.duplicate
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_ALREADY_DEPLOYED EXCEPTION #======================#
    "TeamAlreadyDeployedException",
]

from chess.square import SquareStackException
from chess.system import DebugException


# ======================# TEAM_ALREADY_DEPLOYED EXCEPTION #======================#
class TeamAlreadyDeployedException(SquareStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to deploy a team failed because its members had already been 
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
    ERROR_CODE = "TEAM_ALREADY_DEPLOYED_ERROR"
    DEFAULT_MESSAGE = "Deploying team's members failed: The members were already placed on the board."