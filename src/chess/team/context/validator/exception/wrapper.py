# src/chess/team/context/validator/exception/wrapper.py

"""
Module: chess.team.context.validator.exception.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.team import TeamContextException
from chess.system import ValidationFailedException


__all__ = [
    # ======================# TEAM_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "TeamContextValidationFailedException",
]


# ======================# TEAM_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class TeamContextValidationFailedException(TeamContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a TeamContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   TeamContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "TeamContext validation failed."