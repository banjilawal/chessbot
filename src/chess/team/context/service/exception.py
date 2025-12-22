# src/chess/team/service/exception/base

"""
Module: chess.team.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException
from chess.team import TeamContextException

__all__ = [
    # ======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
    "TeamContextServiceException",
]


# ======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
class TeamContextServiceException(TeamContextException, ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that an TeamContextService encountered an error which prevented the service from completing a task.
    2.  Wrap an exception that hits the try-finally block of an TeamContextService method.

    # PARENT:
        *   ServiceException
        *   TeamContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService raised an exception."