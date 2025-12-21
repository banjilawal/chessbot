# src/chess/team/map/exception.py

"""
Module: chess.team.map.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    # ======================# TEAM_CONTEXT EXCEPTION #======================#
    "TeamContextException",
]


# ======================# TEAM_CONTEXT EXCEPTION #======================#
class TeamContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an TeamContext's organic fields or methods run into a condition that
        leads to an operation failing.
    2.  Parent of exception raised by TeamContext Builders and Validators or any other classes that highly
        cohere with TeamContext objects.
    3.  Catchall for TeamContext errors not covered by lower level  TeamContext exception.

    # PARENT:
        *   ContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "TeamContext raised an exception."