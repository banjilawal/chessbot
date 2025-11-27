# src/chess/agent/context/validator/exception/exception.py

"""
Module: chess.agent.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationException
from chess.agent import AgentContextException

__all__ = [
    # ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidAgentContextException",
]

# ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidAgentContextException(AgentContextException, ValidationException):
    ERROR_CODE = "AGENT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentContext raised an exception."