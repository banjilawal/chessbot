# src/chess/team/service/exception/base

"""
Module: chess.team.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
    "TeamContextServiceException",
]

from chess.system.service.root import ServiceException


# ======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
class TeamContextServiceException(ServiceException):
    """
    # ROLE: Super Exception

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
    ERR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    MSG = "TeamContextService raised an exception."