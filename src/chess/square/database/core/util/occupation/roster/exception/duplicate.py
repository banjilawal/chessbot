# src/chess/square/database/core/exception/deployment/duplicate.py

"""
Module: chess.square.database.core.exception.deployment.duplicate
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_ALREADY_DEPLOYED EXCEPTION #======================#
    "RosterDoubleDeploymentException",
]

from chess.square import SquareStackServiceException
from chess.system import DebugException


# ======================# TEAM_ALREADY_DEPLOYED EXCEPTION #======================#
class RosterDoubleDeploymentException(SquareStackServiceException, DebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure UpdateResult was returned because the roster was not at full capacity when
    its formation on the board was attempted.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CANNOT_DEPLOY_UNDER_STRENGTH_TEAM_ERROR"
    DEFAULT_MESSAGE = "Roster deployment failed: The roster did not have all 16 members available."
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to deploy a team failed because its members had already been 
        placed on the board.

    # PARENT:
        *   SquareStackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_ALREADY_DEPLOYED_ERROR"
    DEFAULT_MESSAGE = "Deploying team's members failed: The members were already placed on the board."