# src/chess/team/service/data/exception.py

"""
Module: chess.team.service.data.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import DataServiceException, NullException

__all__ = [
    "TeamDataServiceException",
    "TeamNullDataSetException"
]


class TeamDataServiceException(DataServiceException):
    ERROR_CODE = "TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamDataService raised an exception."


class TeamNullDataSetException(TeamDataServiceException, NullException):
    ERROR_CODE = "TEAM_NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "TeamDataService cannot have a null list of items."