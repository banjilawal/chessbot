# src/chess/agent/map/validator/exception/flag/zero.py

"""
Module: chess.agent.map.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.system import ContextFlagCountException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= ZERO_AGENT_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroAgentContextFlagsException"
]


# ========================= ZERO_AGENT_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroAgentContextFlagsException(InvalidAgentContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no AgentContext flag was enabled. One and only one Agent attribute-value-tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidAgentContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_AGENT_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero AgentContext flags were set. Cannot search for Agents if one-and_oly-one "
        "map flag is enabled."
    )