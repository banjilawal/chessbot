# src/chess/agent/context/number_bounds_validator/exception/flag/excess.py

"""
Module: chess.agent.context.number_bounds_validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BoundsException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= EXCESSIVE_AGENT_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveAgentContextFlagsException"
]


# ========================= EXCESSIVE_AGENT_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveAgentContextFlagsException(InvalidAgentContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one AgentContext flag was enabled. Only one Agent attribute-value tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_AGENT_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive AgentContext flags were set. Only one AgentContext flag is allowed."