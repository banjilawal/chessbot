# src/chess/team/service/exception/base.py

"""
Module: chess.team.service.exception.base
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import ServiceException

__all__ = [
    # ======================# TEAM_SERVICE EXCEPTIONS #======================#
    "TeamServiceException",
]


# ======================# TEAM_SERVICE EXCEPTIONS #======================#
class TeamServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamService objects.
    2.  Raised when an exception hits the try-finally block of a TeamService method.
    3.  Catchall for TeamService failures that are not covered by a lower level TeamService exceptions.

    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SERVICE_ERROR"
    DEFAULT_ERROR_CODE = "TeamService raised an exception."