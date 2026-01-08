# src/chess/team/hostage/exception/insertion/wrapper.py

"""
Module: chess.team.hostage.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import HostageServiceException

__all__ = [
    # ======================# HOSTAGE_ADDITION_FAILURE #======================#
    "AddingHostageTokenFailedException",
]


# ======================# HOSTAGE_ADDITION_FAILURE EXCEPTION #======================#
class AddingHostageTokenFailedException(HostageServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that add a token to the hostage failed.

    # PARENT:
        *  HostageServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_ADDITION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Adding prisoner failed."