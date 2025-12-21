# src/chess/team/map/finder/exception/dataset.py

"""
Module: chess.team.map.finder.exception.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import DataException, NullException


__all__ = [
    "TeamSearchDatasetNullException",
]

#======================# TEAM_NULL_DATASET EXCEPTION #======================#
class TeamSearchDatasetNullException(DataException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates TeamFinder received null instead of a List[Team] collection.

    # PARENT:
        *   DataException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SEARCH_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = (
        "TeamFinder needs a list of teams to run serach operations on. Cannot pass pass null "
        "as the List[Team] collection."
    )