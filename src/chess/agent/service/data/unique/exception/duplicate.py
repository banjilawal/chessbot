# src/chess/player_agent/service/data/unique/exception/duplicate.py

"""
Module: chess.player_agent.service.data.unique.exception.duplicate
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import UniqueAgentDataServiceException


__all__ = [
    #======================# ADDING_DUPLICATE_AGENT EXCEPTION #======================#
    "AddingDuplicateAgentException",
]


#======================# ADDING_DUPLICATE_AGENT EXCEPTION #======================#
class AddingDuplicateAgentException(UniqueAgentDataServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    Indicate an attempt was made to add an PlayerAgent that already exists in the dataset.

    # PARENT:
        *   UniqueAgentDataServiceException

    # PROVIDES:
    AddingDuplicateAgentException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "DUPLICATE_AGENT_ADDITION_ERROR"
    DEFAULT_MESSAGE = "UniqueAgentDataService cannot add duplicate Agents to the list."