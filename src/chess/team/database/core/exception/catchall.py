# src/chess/team/database/core/exception/catchall.py

"""
Module: chess.team.database.core.exception.catchall
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_STACK_SERVICE EXCEPTION #======================#
    "TeamStackException",
]

from chess.team import TeamException
from chess.system import StackException


# ======================# TEAM_STACK_SERVICE EXCEPTION #======================#
class TeamStackException(TeamException, StackException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Encapsulate TeamStack method outputs when there is a failure.

    # PARENT:
        *   TeamException
        *   StackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_STACK_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamStack raised an exception."