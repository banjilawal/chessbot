# src/chess/agent/context/validator/exception/flag/base.py

"""
Module: chess.agent.context.validator.exception.flag.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= AGENT_CONTEXT FLAG EXCEPTIONS =========================#
    "NoAgentContextFlagException",
    "TooManyAgentContextFlagsException"
]


# ========================= AGENT_CONTEXT FLAG EXCEPTIONS =========================#
class NoAgentContextFlagException(InvalidAgentContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, AgentContextException

    # RESPONSIBILITIES:
    1.  Raised if no AgentContext flag is provided with a searcher value.
    
    # PARENT
        *   InvalidAgentContextException
        *   ContextFlagCountException

    # PROVIDES:
    NoAgentContextFlagException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_AGENT_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No AgentContext flag was selected. A context flag must be turned on with a target value."


class TooManyAgentContextFlagsException(InvalidAgentContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, AgentContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Agent attribute is going to be used in an AgentFinder.
    
    # PARENT
        *   InvalidAgentContextException
        *   ContextFlagCountException

    # PROVIDES:
    TooManyAgentContextFlagsException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOO_MANY_AGENT_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one AgentContext flag was selected. Only one context flag is allowed."
