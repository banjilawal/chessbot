# src/chess/player/validator/exception/flag/excess.py

"""
Module: chess.player.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.agent import InvalidAgentContextException

__all__ = [
    # ========================= ARENA_AGENT_CONTEXT_FLAG EXCEPTION =========================#
    "ArenaAgentContextFlagsException"
]


# ========================= ARENA_AGENT_CONTEXT_FLAG EXCEPTION =========================#
class ArenaAgentContextFlagsException(InvalidAgentContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one AgentContext flag was enabled. Only one Agent attribute-value-tuple can be used in
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   PlayerContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_AGENT_CONTEXT_FLAG_EXCEPTION"
    MSG = (
        "Arena AgentContext flags were set. an Agent search can only use one-and-only "
        "map flag at a time."
    )