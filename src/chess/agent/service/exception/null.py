# src/chess/agent/service//exception/null.py

"""
Module: chess.agent.service..exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentServiceException


__all__ = [
    "NullAgentServiceException",
]


#======================# NULL AGENT_SERVICE EXCEPTION #======================#
class NullAgentServiceException(InvalidAgentServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an AgentService but got null instead.

    # PARENT:
        *   InvalidAgentServiceException
        *   NullException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentService cannot be null."
