# src/chess/game/finder/exception/dataset.py

"""
Module: chess.game.finder.exception.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import DataException, NullException


__all__ = [
    "GameSearchDataSetNullException",
]

#======================# GAME_NULL_DATASET EXCEPTION #======================#
class GameSearchDataSetNullException(DataException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates GameFinder received null instead of a List[Game] collection.

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
    ERROR_CODE = "GAME_SEARCH_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = (
        "GameFinder needs a list of games to run serach operations on. Cannot pass pass null "
        "as the List[Game] collection."
    )