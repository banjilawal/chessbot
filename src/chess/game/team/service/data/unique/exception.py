# src/chess/team/service/data/unique/base.py

"""
Module: chess.team.entity_service.data.unique.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import UniqueDataServiceException

__all__ = [
    # ======================# UNIQUE_TEAM_DATA_SERVICE EXCEPTIONS #======================#
    "UniqueTeamDataServiceException",
]


# ======================# UNIQUE_TEAM_DATA_SERVICE EXCEPTIONS #======================#
class UniqueTeamDataServiceException(UniqueDataServiceException):
    """
    Raised when internal components are null or raise system errors. Not appropriate
    for CRUD exceptions.
    """
    ERROR_CODE = "UNIQUE_TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueTeamDataService raised an exception."