# src/chess/team/context/service/exception.py

"""
Module: chess.team.context.service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ========================= TEAM_CONTEXT_SERVICE EXCEPTIONS =========================#
    "TeamContextServiceException",
]


# ========================= TEAM_CONTEXT_SERVICE EXCEPTIONS =========================#
class TeamContextServiceException(ServiceException):
    """
    Catchall Exception for TeamContextService when either TeamContextService.builder or
    TeamContextService.validator raise an unhandled exception.
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService raised an exception."