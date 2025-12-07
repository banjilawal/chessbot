# src/chess/agent/model/variety/exception/null.py

"""
Module: chess.agent.model.variety.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentVarietyException

__all__ = [
    # ======================# AGENT_VARIETY NULL EXCEPTION #======================#
    "AgentVarietyNullException",
]

# ======================# NULL AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyNullException(InvalidAgentVarietyException, NullException):
    """"""
    ERROR_CODE = "NULL_AGENT_VARIETY_ERROR"
    DEFAULT_MESSAGE = "AgentVariety cannot be null."


