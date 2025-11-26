# src/chess/team/context/service/exception.py

"""
Module: chess.team.context.service.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    "TeamContextServiceException",
]


class TeamContextServiceException(ServiceException):
    """
    Super class of exceptions raised by TeamContextService objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService raised an exception."