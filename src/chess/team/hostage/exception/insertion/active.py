# src/chess/team/prisoner/exception/insertion/active.py

"""
Module: chess.team.prisoner.exception.insertion.active
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# ADDING_ACTIVE_TOKEN_TO_HOSTAGES EXCEPTION #======================#
    "AddingActiveTokenException",
]

from chess.team import HostageServiceException


# ======================# ADDING_ACTIVE_TOKEN_TO_HOSTAGES EXCEPTION #======================#
class AddingActiveTokenException(HostageServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be added to t

    # PARENT:
        *   HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_ACTIVE_TOKEN_TO_HOSTAGES_ERROR"
    DEFAULT_MESSAGE = "Adding prisoner failed: An active token cannot be made a prisoner."