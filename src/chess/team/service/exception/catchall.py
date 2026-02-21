# src/chess/team/service/exception/catchall.py

"""
Module: chess.team.service.exception.catchall
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ServiceException
from chess.team import TeamException

__all__ = [
    # ======================# TEAM_SERVICE EXCEPTION #======================#
    "TeamServiceException",
]


# ======================# TEAM_SERVICE EXCEPTION #======================#
class TeamServiceException(TeamException, ServiceException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Encapsulate TeamService method outputs when there is a failure.

    # PARENT:
        *   ServiceException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamService raised an exception."