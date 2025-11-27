# src/chess/agent/validator/exception/null/exception.py

"""
Module: chess.agent.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentException

__all__ = [
    # ======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
    "NullAgentException",
]

# ======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
class NullAgentException(InvalidAgentException, NullException):
    """Raised if an entity, method, or operation requires an Agent but gets null instead."""
    ERROR_CODE = "NULL_AGENT_ERROR"
    DEFAULT_MESSAGE = "Agent cannot be null."