# src/model/state/binder/validation/validator.py

"""
Module: model.state.binder.validation.work
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_VALIDATION_FAILURE #======================#
    "TeamBinderValidatorException",
]

from model.state.team import TeamBinderException
from system import ValidatorException



# ======================# TEAM_BINDER_VALIDATION_FAILURE #======================#
class TeamBinderValidatorException(TeamBinderException, ValidatorException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a rank failed its validation as a Team. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   TeamBinderException
        *   ValidatorException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_VALIDATION_FAILURE"
    MSG = "TeamBinder validation failed."