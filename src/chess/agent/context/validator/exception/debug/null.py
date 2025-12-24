# src/chess/agent/validator/exception/null.py

"""
Module: chess.agent.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentContextException

__all__ = [
    #======================# AGENT_CONTEXT NULL EXCEPTION #======================#
    "NullAgentContextException",
]

#======================# AGENT_CONTEXT NULL EXCEPTION #======================#
class NullAgentContextException(InvalidAgentContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an AgentContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an AgentContext but receives null instead.
    
    # PARENT:
        *   InvalidAgentContextException
        *   NullAgentContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentContext cannot be null."
    
    
    