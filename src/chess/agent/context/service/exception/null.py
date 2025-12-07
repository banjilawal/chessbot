# src/chess/agent/context/service/exception/null.py

"""
Module: chess.agent.context.service.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentContextServiceException

__all__ = [
    # ======================# NULL AGENT_CONTEXT_SERVICE EXCEPTIONS #======================#
    "NullAgentContextServiceException",
]


# ======================# NULL AGENT_CONTEXT_SERVICE EXCEPTION #======================#
class NullAgentContextServiceException(InvalidAgentContextServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an AgentContextService but got null instead.
    
    # PARENT
        *   InvalidAgentContextServiceException
        *   NullException

    # PROVIDES:
    NullAgentContextServiceException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "AgentContextService cannot be null."