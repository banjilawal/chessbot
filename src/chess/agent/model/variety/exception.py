# src/chess/agent/model/variety.exception.py

"""
Module: chess.agent.model.variety.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ChessException, NullException

__all__ = [
# ======================# AGENT_VARIETY EXCEPTION #======================#
    "AgentVarietyException",
    
# ======================# AGENT_VARIETY NULL EXCEPTION #======================#
    "AgentVarietyNullException",
]


# ======================# AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyException(ChessException):
    """
    Super class for exceptions raised by AgentVariety objects. DO NOT USE DIRECTLY. Subclasses
    give more useful debugging messages.
    """
    ERROR_CODE = "AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety raised an exception."


# ======================# AGENT_VARIETY NULL EXCEPTION  #======================#
class AgentVarietyNullException(AgentVarietyException, NullException):
    """"""
    ERROR_CODE = "NULL_AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety cannot be null."