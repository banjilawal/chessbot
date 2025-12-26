# src/chess/team/service/data/unique/exception/catchall.py

"""
Module: chess.team.service.data.unique.exception.catchall
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_DATA_SERVICE EXCEPTION #======================#
    "UniqueTeamDataServiceException",
]

from chess.team import TeamException
from chess.system import ServiceException


# ======================# UNIQUE_TEAM_DATA_SERVICE EXCEPTION #======================#
class UniqueTeamDataServiceException(TeamException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an UniqueTeamDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a UniqueTeamDataService method.

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
    ERROR_CODE = "UNIQUE_TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueTeamDataService raised an exception."