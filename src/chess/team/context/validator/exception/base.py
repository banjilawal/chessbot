# src/chess/team/map/validator/exception/exception.py

"""
Module: chess.team.map.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.team import TeamContextException

__all__ = [
    #======================# TEAM_CONTEXT VALIDATION EXCEPTION #======================#
    "InvalidTeamContextException",
]

#======================# TEAM_CONTEXT VALIDATION EXCEPTION #======================#
class InvalidTeamContextException(TeamContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised TeamContext validation.
    2.  Wraps unhandled exceptions that hit the finally-block in TeamContextValidator methods.
    
    # PARENT:
        *   TeamContextException
        *   ValidationFailedException

    # PROVIDES:
    InvalidTeamContextException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamContext validation failed."
