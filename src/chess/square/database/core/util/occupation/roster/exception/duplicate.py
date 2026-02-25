# src/chess/square/database/core/exception/deployment/duplicate.py

"""
Module: chess.square.database.core.exception.deployment.duplicate
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_DOUBLE_DEPLOYMENT EXCEPTION #======================#
    "RosterDoubleDeploymentException",
]

from chess.square import SquareDebugException


# ======================# ROSTER_DOUBLE_DEPLOYMENT EXCEPTION #======================#
class RosterDoubleDeploymentException(SquareDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failing UpdateResult was returned because an attempt was made to deploy a team
    after its roster had already been formed on the board.

    # PARENT:
        *   SquareDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "CANNOT_DEPLOY_UNDER_STRENGTH_TEAM_ERROR"
    MSG = "Roster deployment failed: The roster had already been deployed on the board."
