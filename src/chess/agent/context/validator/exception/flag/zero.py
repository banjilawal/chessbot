# src/chess/agent/context/validator/exception/flag/zero.py

"""
Module: chess.agent.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import BoundsException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= ZERO_AGENT_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroAgentContextFlagsSetException"
]


# ========================= ZERO_AGENT_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroAgentContextFlagsSetException(InvalidAgentContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no AgentContext flag was enabled. One and only one Agent attribute-value tuple is required for
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidAgentContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_AGENT_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "Zero AgentContext flags were set. One and only one context flag must be enabled,"