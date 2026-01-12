# src/chess/owner/model/variety/exception/exception.py

"""
Module: chess.owner.model.variety.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    #======================# PLAYER_VARIETY EXCEPTION #======================#
    "AgentVarietyException",
]


#======================# PLAYER_VARIETY EXCEPTION  #======================#
class AgentVarietyException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised when an AgentVariety's normal operations are halted by an error condition.
    2.  Raised when no specific exception exists for the condition which brought the AgentVariety object into
        an error state.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety raised an exception."