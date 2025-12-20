# src/chess/agent/context/finder/exception/dataset.py

"""
Module: chess.agent.cntext.finder.exception.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.agent import AgentException
from chess.system import NullDataSetException

__all__ = [
    "AgentSearchDatasetNullException",
]




# ======================# AGENT_NULL_DATASET EXCEPTION #======================#
class AgentSearchDatasetNullException(AgentException, NullDataSetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates AgentFinder received null instead of a List[Agent] collection.

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
    ERROR_CODE = "AGENT_SEARCH_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = (
        "AgentFinder needs a list of agents to run serach operations on. Cannot pass pass null "
        "as the List[Agent] collection."
    )