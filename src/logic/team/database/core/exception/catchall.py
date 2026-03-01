# src/logic/team/database/core/exception/super.py

"""
Module: logic.team.database.core.exception.super
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_STACK_SERVICE EXCEPTION #======================#
    "TeamStackException",
]

from logic.team import TeamException
from logic.system import StackServiceException


# ======================# TEAM_STACK_SERVICE EXCEPTION #======================#
class TeamStackException(TeamException, StackServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Encapsulate TeamStack method outputs when there is a failure.

    # PARENT:
        *   TeamException
        *   StackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_STACK_SERVICE_EXCEPTION"
    MSG = "TeamStack raised an exception."