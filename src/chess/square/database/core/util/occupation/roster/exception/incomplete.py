# src/chess/square/database/core/exception/deployment/incomplete.py

"""
Module: chess.square.database.core.exception.deployment.incomplete
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_DEPLOYMENT_INTERRUPTED EXCEPTION #======================#
    "RosterDeploymentInterruptedException",
]

from chess.square import SquareDebugException


# ======================# ROSTER_DEPLOYMENT_INTERRUPTED EXCEPTION #======================#
class RosterDeploymentInterruptedException(SquareDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    A failure UpdateResult was returned because one of the roster members failed its attempt to
    occupy its opening square.

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
    DEFAULT_MESSAGE = "Roster deployment failed: A failed square occupation interrupted the roster's deployment."