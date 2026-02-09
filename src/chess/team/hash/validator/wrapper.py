# src/chess/team/hash/validator/wrapper.py

"""
Module: chess.team.hash.validator.wrapper
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_VALIDATION_FAILURE EXCEPTION #======================#
    "TeamHashValidationFailedException",
]

from chess.team import TeamHashException
from chess.system import ValidationFailedException



# ======================# TEAM_HASH_VALIDATION_FAILURE EXCEPTION #======================#
class TeamHashValidationFailedException(TeamHashException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a Team. The exception chain 
        traces the ultimate source of failure.

    # PARENT:
        *   TeamHashException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_HASH_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TeamHash validation failed."