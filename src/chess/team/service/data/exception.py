# src/chess/team/service/data/exception/service/exception.py

"""
Module: chess.team.service.data.exception.service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import DataServiceException, NullException

_
___all__ = [
    # ======================# TEAM_DATA_SERVICE EXCEPTION #======================#
    "TeamDataServiceException",
]

from chess.team import TeamException
from chess.system import ServiceException


# ======================# TEAM_DATA_SERVICE EXCEPTION #======================#
class TeamDataServiceException(TeamException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an TeamDataService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of a TeamDataService method.

    # PARENT:
        *   ServiceException
        *   TeamDataException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamDataService raised an exception."