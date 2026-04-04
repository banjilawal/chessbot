# src/model/team/hash/validation/validator.py

"""
Module: model.team.hash.validation.work
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_VALIDATION_FAILURE #======================#
    "TeamHashValidationException",
]

from model.team import TeamHashException
from system import ValidationException



# ======================# TEAM_HASH_VALIDATION_FAILURE #======================#
class TeamHashValidationException(TeamHashException, ValidationException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why a rank failed its validation as a Team. The exception chain
        traces the ultimate source of failure.

    Super Class:
        *   TeamHashException
        *   ValidationException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_HASH_VALIDATION_FAILURE"
    MSG = "TeamHash validation failed."