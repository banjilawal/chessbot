# src/chess/team/hostage/exception/catchall.py

"""
Module: chess.team.hostage.exception.catchall
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException

__all__ = [
    # ======================# HOSTAGE_SERVICE EXCEPTION #======================#
    "HostageServiceException",
]


# ======================# HOSTAGE_SERVICE EXCEPTION #======================#
class HostageServiceException(TeamException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for HostageService errors.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "HostageService raised an exception."