# src/chess/agent/context/validator/exception/null/exception.py

"""
Module: chess.agent.context.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
    "NullAgentContextException",
]

# ======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
class NullAgentContextException(InvalidAgentContextException, NullException):
    """Raised if an entity, method, or operation requires an AgentContext but gets null instead."""
    ERROR_CODE = "NULL_AGENT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentContext cannot be null."