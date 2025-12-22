# src/chess/agent/map/validator/exception/flag/excess.py

"""
Module: chess.agent.map.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= EXCESSIVE_AGENT_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveAgentContextFlagsException"
]


# ========================= EXCESSIVE_AGENT_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveAgentContextFlagsException(InvalidAgentContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one AgentContext flag was enabled. Only one Agent attribute-value-tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_AGENT_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive AgentContext flags were set. an Agent search can only use one-and-only "
        "map flag at a time."
    )