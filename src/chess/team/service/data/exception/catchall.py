# src/chess/team/service/data/exception/catchall.py

"""
Module: chess.team.service.data.exception.catchall
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_DATA_SERVICE EXCEPTION #======================#
    "TeamDataServiceException",
]

from chess.team import TeamException
from chess.system import DataServiceException


# ======================# TEAM_DATA_SERVICE EXCEPTION #======================#
class TeamDataServiceException(TeamException, DataServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Encapsulate TeamDataService method outputs when there is a failure.

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
    ERROR_CODE = "TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamDataService raised an exception."