# src/chess/team/searcher/exception.py

"""
Module: chess.team.searcher.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import SearchException

__all__ = [
    # ======================# TEAM_SEARCH EXCEPTIONS #======================#
    "TeamSearchException",
    "TeamSearchFailedException",
]


# ======================# TEAM_SEARCH EXCEPTIONS #======================#
class TeamSearchException(SearchException):
    """
    Super class of exceptions raised by TeamSearch objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "TEAM_SEARCH_ERROR"
    DEFAULT_MESSAGE = "TeamSearch raised an exception."


class TeamSearchFailedException(TeamSearchException):
    """"""
    ERROR_CODE = "TEAM_SEARCH_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamSearch failed."
