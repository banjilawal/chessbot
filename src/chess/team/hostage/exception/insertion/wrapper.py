# src/chess/team/prisoner/exception/insertion/wrapper.py

"""
Module: chess.team.prisoner.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import HostageServiceException

__all__ = [
    # ======================# HOSTAGE_ADDITION_FAILURE #======================#
    "AddingHostageTokenFailedException",
]


# ======================# HOSTAGE_ADDITION_FAILURE #======================#
class AddingHostageTokenFailedException(HostageServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a occupant to the prisoner failed.

    # PARENT:
        *  HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_ADDITION_FAILURE"
    DEFAULT_MESSAGE = "Adding prisoner failed."