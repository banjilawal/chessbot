# src/logic/owner/model/variety/exception/null.py

"""
Module: logic.owner.model.variety.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from system import NullException
from logic.agent import InvalidAgentVarietyException


__all__ = [
    #======================# PLAYER_VARIETY NULL EXCEPTION #======================#
    "AgentVarietyNullException",
]

#======================# NULL AGENT_VARIETY EXCEPTION  #======================#
class AgentVarietyNullException(InvalidAgentVarietyException, NullException):
    """
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate if an entity, method or operation required an AgentVariety  but got null instead.

    Super Class:
        *   InvalidAgentVarietyException
        *   NullException

    Provides:

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_AGENT_VARIETY_EXCEPTION"
    MSG = "AgentVariety cannot be null."


