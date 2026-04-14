# src/model/binder/validation/validator.py

"""
Module: model.binder.validation.work
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER_VALIDATION_FAILURE #======================#
    "TeamBinderValidationException",
]

from model.team import TeamBinderException
from system import ValidationException



# ======================# TEAM_BINDER_VALIDATION_FAILURE #======================#
class TeamBinderValidationException(TeamBinderException, ValidationException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a rank failed its validation as a Team. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   TeamBinderException
        *   ValidationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_VALIDATION_FAILURE"
    MSG = "TeamBinder validation failed."