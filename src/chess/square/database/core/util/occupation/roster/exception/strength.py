# src/chess/square/database/core/exception/deployment/strength.py

"""
Module: chess.square.database.core.exception.deployment.strength
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# CANNOT_DEPLOY_UNDER_STRENGTH_TEAM EXCEPTION #======================#
    "CannotDeployUnderStrengthTeamException",
]

from chess.square import SquareDebugException


# ======================# CANNOT_DEPLOY_UNDER_STRENGTH_TEAM EXCEPTION #======================#
class CannotDeployUnderStrengthTeamException(SquareDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    A failing UpdateResult was returned because the roster was not at full capacity when
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
    ERR_CODE = "CANNOT_DEPLOY_UNDER_STRENGTH_TEAM_EXCEPTION"
    MSG = "Roster deployment failed: The roster did not have all 16 members available."