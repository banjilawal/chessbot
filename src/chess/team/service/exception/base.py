# src/chess/team/service/exception/base.py

"""
Module: chess.team.service.exception.base
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
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an TeamService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a TeamService method.

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