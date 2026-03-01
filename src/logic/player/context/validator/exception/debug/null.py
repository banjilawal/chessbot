# src/logic/player/validator/exception/null.py

"""
Module: logic.player.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_AGENT_CONTEXT EXCEPTION #======================#
    "NullAgentContextException",
]

from logic.system import NullException
from logic.agent import InvalidAgentContextException


# ======================# NULL_AGENT_CONTEXT EXCEPTION #======================#
class NullAgentContextException(InvalidAgentContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that AgentContext validation failed because the candidate was null.

    # PARENT:
        *   NullAgentContextException
        *   PlayerContextValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NULL_AGENT_CONTEXT_EXCEPTION"
    MSG = "AgentContext validation failed: The candidate was null."