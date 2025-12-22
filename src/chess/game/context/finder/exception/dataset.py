# src/chess/game/finder/exception/dataset.py

"""
Module: chess.game.finder.exception.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.game import GameException
from chess.system import NullDatasetException


__all__ = [
    # ======================# GAME_NULL_DATASET EXCEPTION #======================#
    "GameSearchDatasetNullException",
]




#======================# GAME_NULL_DATASET EXCEPTION #======================#
class GameSearchDatasetNullException(GameException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  GameFinder received null instead of a List[Game] collection.

    # PARENT:
        *   DatasetException
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