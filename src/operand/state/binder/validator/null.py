# src/operand/state/binder/validation/null.py

"""
Module: operand.state.binder.validation.null
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_NULL_EXCEPTION EXCEPTION #======================#
    "TeamBinderNullException",
]

from system import NullException
from operand.state.team import TeamBinderException


# ======================# TEAM_BINDER_NULL_EXCEPTION EXCEPTION #======================#
class TeamBinderNullException(TeamBinderException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that the rank was not validated as a TeamBinder because it was null.

    Super Class:
        *   NullException
        *   TeamBinderException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_NULL_EXCEPTION_EXCEPTION"
    MSG = "TeamBinder validation failed: The rank was null."