# src/chess/team/context/exception.py

"""
Module: chess.team.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    "TeamContextException",
]

#======================# TEAM_CONTEXT EXCEPTIONS #======================#
class TeamContextException(ContextException):
    """Catchall Exception for TeamContextBuilder when it encounters an error building a Team."""
    ERROR_CODE = "TEAM_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamContext raised an exception."