# src/chess/square/database/core/exception/deployment/wrapper.py

"""
Module: chess.square.database.core.exception.deployment.wrapper
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

__all__ = [
    # ======================# ROSTER_DEPLOYMENT_FAILURE #======================#
    "RosterDeploymentException",
]

from chess.system import UpdateException


# ======================# ROSTER_DEPLOYMENT_FAILURE #======================#
class RosterDeploymentException(UpdateException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in RosterDeployer.form_team that prevented a successful UpdateResult.

    # PARENT:
        *   UpdateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ROSTER_DEPLOYMENT_FAILURE"
    MSG = "Roster deployment failed."

