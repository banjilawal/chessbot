# src/chess/team/searcher/exception.py

"""
Module: chess.team.searcher.exception
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    # ======================# TEAM_SEARCH EXCEPTIONS #======================#
    "TeamFinderException",
    "TeamSearchFailedException",
]


# ======================# TEAM_SEARCH EXCEPTIONS #======================#
class TeamFinderException(FinderException):
    """
    Super class of exceptions raised by TeamFinder objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "TEAM_SEARCH_ERROR"
    DEFAULT_MESSAGE = "TeamFinder raised an exception."


class TeamSearchFailedException(TeamFinderException):
    """"""
    ERROR_CODE = "TEAM_SEARCH_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamFinder failed."
