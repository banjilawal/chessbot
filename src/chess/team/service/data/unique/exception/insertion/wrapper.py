# src/chess/team/service/data/exception/insertion/wrapper.py

"""
Module: chess.team.service.data.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_INSERTION_FAILURE EXCEPTION #======================#
    "TeamInsertionFailedException",
]

from chess.system import InsertionFailedException


# ======================# TEAM_INSERTION_FAILURE EXCEPTION #======================#
class TeamInsertionFailedException(InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why TeamDataService could not delete a team. The encapsulated 
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_INSERTION_FAILURE"
    DEFAULT_MESSAGE = "Team insertion failed."