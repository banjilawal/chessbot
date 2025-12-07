# src/chess/team/context/validator/exception/null/base.py

"""
Module: chess.team.context.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamContextException

__all__ = [
    # ========================= NULL TEAM_CONTEXT EXCEPTIONS =========================#
    "NullTeamContextException"
]

# ========================= NULL TEAM_CONTEXT EXCEPTIONS =========================#
class NullTeamContextException(InvalidTeamContextException, NullException):
    """Raised if an entity, method, or operation requires TeamContext but gets null instead."""
    ERROR_CODE = "NULL_TEAM_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamContext cannot be null."