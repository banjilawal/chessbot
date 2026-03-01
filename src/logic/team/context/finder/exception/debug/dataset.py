# src/logic/team/context/finder/exception/debug/dataset.py

"""
Module: logic.team.context.finder.exception.debug.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""




__all__ = [
    "TeamSearchDatasetNullException",
]

from logic.team import Team
from logic.system import NullDatasetException

#======================# TEAM_NULL_DATASET EXCEPTION #======================#
class TeamSearchDatasetNullException(Team, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That TeamFinder received null instead of a List[Team] collection.

    # PARENT:
        *   CollectionException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_SEARCH_DATASET_NULL_EXCEPTION"
    MSG = "TeamSearch failed: Cannot run a search on a null dataset."
 