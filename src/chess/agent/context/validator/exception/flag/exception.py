# src/chess/agent/context/validator/exception/flag/exception.py

"""
Module: chess.agent.context.validator.exception.flag.__init__
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BoundsException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= AGENT_CONTEXT FLAG EXCEPTIONS =========================#
    "NoAgentContextFlagSetException",
    "TooManyAgentContextFlagsSetException"
]

# ========================= AGENT_CONTEXT FLAG EXCEPTIONS =========================#
class NoAgentContextFlagSetException(InvalidAgentContextException, BoundsException):
    """Raised if no AgentContext was selected."""
    ERROR_CODE = "NO_AGENT_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "One and only one, AgentContext flag must be set."


class TooManyAgentContextFlagsSetException(InvalidAgentContextException, BoundsException):
    """Raised if too many AgentContext flags were set."""
    ERROR_CODE = "AGENT_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one AgentContext flag can be set."
