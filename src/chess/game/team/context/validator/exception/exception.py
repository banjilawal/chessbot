# src/chess/team/context/validator/base.py

"""
Module: chess.team.context.validator.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamContextException
from chess.system import ValidationException


__all__ = [
# ========================= TEAM_CONTEXT VALIDATION EXCEPTION SUPER CLASS  =========================#
    "InvalidTeamContextException",
]


# ========================= TEAM_CONTEXT VALIDATION EXCEPTION SUPER CLASS  =========================#
class InvalidTeamContextException(TeamContextException, ValidationException):
    """Catchall Exception for TeamContextValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "TEAM_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamContext validation failed."