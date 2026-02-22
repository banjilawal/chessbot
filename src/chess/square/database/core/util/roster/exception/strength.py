# src/chess/square/database/core/exception/deployment/strength.py

"""
Module: chess.square.database.core.exception.deployment.strength
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_PARTIALLY_DEPLOYED EXCEPTION #======================#
    "CannotDeployUnderStrengthTeamException",
]

from chess.square import SquareStackException
from chess.system import DebugException


# ======================# TEAM_PARTIALLY_DEPLOYED EXCEPTION #======================#
class CannotDeployUnderStrengthTeamException(SquareStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to deploy a team failed because it did not have a full complement of tokens.

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
    DEFAULT_MESSAGE = (
        "Deploying team's members failed: A team must have a full complement of tokens before it can be deployed."
    )