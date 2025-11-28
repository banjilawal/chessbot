# src/chess/team/service/data/unique/exception.py

"""
Module: chess.team.service.data.unique.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import UniqueDataServiceException

__all__ = [
    # ======================# UNIQUE_TEAM_DATA_SERVICE EXCEPTIONS #======================#
    "UniqueTeamDataServiceException",
    "AddingDuplicateTeamException",
]


# ======================# UNIQUE_TEAM_DATA_SERVICE EXCEPTIONS #======================#
class UniqueTeamDataServiceException(UniqueDataServiceException):
    """
    Super class of exceptions raised by UniqueTeamDataService objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "UNIQUE_TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "UniqueTeamDataService raised an exception."


class AddingDuplicateTeamException(UniqueTeamDataServiceException):
    """Raised when trying to add a duplicate Team to a list of Teams."""
    ERROR_CODE = "DUPLICATE_TEAM_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueTeamDataService cannot add duplicate Teams to the list."