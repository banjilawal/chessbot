# src/chess/owner/finder/exception/dataset.py

"""
Module: chess.owner.cntext.finder.exception.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.agent import AgentException
from chess.system import NullDatasetException

__all__ = [
    "AgentSearchDatasetNullException",
]




# ======================# PLAYER_NULL_DATASET EXCEPTION #======================#
class AgentSearchDatasetNullException(AgentException, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  AgentFinder received null instead of a List[Agent] collection.

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
    ERROR_CODE = "AGENT_SEARCH_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = (
        "AgentFinder needs a list of agents to run serach operations on. Cannot pass pass null "
        "as the List[Agent] collection."
    )