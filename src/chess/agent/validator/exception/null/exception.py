# src/chess/agent/validator/exception/null/exception.py

"""
Module: chess.agent.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentException, AgentTypeException

__all__ = [
    # ======================# AGENT NULL EXCEPTIONS #======================#
    "NullAgentException",
    "NullAgentTypeException",
]

# ======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
class NullAgentException(InvalidAgentException, NullException):
    """Raised if an entity, method, or operation requires an Agent but gets null instead."""
    ERROR_CODE = "NULL_AGENT_ERROR"
    DEFAULT_MESSAGE = "Agent cannot be null."


class NullAgentTypeException(AgentTypeException, NullException):
    """Raised if an entity, method, or operation requires an AgentVariety but gets null instead."""
    ERROR_CODE = "NULL_AGENT_TYPE_ERROR"
    DEFAULT_MESSAGE = "AgentVariety cannot be null."