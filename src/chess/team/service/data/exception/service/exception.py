# src/chess/team/service/data/exception/service/exception.py

"""
Module: chess.team.service.data.exception.service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import DataServiceException, NullException

__all__ = [
#======================# TEAM_DATA_SERVICE EXCEPTION SUPER CLASS #======================#
    "TeamDataServiceException",
    "TeamStackNullException",
    "TeamContextServiceNullException",
    "TeamSearchNullException",
    "TeamServiceNullException",
]


#======================# TEAM_DATA_SERVICE EXCEPTION SUPER CLASS #======================#
class TeamDataServiceException(DataServiceException):
    """
    Catchall for exceptions which aren't about inserting or deleting Teams. Wrapper for
    component entity_service reliability failures.
    """
    ERROR_CODE = "TEAM_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamDataService raised an exception."


class TeamStackNullException(TeamDataServiceException, NullException):
    """Raised if the internal stack is null"""
    ERROR_CODE = "TEAM_STACK_NULL_ERROR"
    DEFAULT_MESSAGE = "TeamDataService cannot have a null stack."


class TeamContextServiceNullException(TeamDataServiceException, NullException):
    """Raised if the internal TeamContextService  is null"""
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_NULL_ERROR"
    DEFAULT_MESSAGE = "TeamDataService cannot have a null TeamContextService."


class TeamSearchNullException(TeamDataServiceException, NullException):
    """Raised if the internal TeamFinder object  is null"""
    ERROR_CODE = "TEAM_SEARCH_NULL_ERROR"
    DEFAULT_MESSAGE = "TeamDataService cannot have a null TeamFinder object."


class TeamServiceNullException(TeamDataServiceException, NullException):
    """Raised if the internal TeamCertifier object  is null"""
    ERROR_CODE = "TEAM_SERVICE_NULL_ERROR"
    DEFAULT_MESSAGE = "TeamDataService cannot have a null TeamCertifier."