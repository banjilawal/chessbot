# src/chess/player/validator/exception/null.py

"""
Module: chess.player.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# NULL_AGENT_CONTEXT EXCEPTION #======================#
    "NullAgentContextException",
]

from chess.system import NullException
from chess.agent import InvalidAgentContextException


# ======================# NULL_AGENT_CONTEXT EXCEPTION #======================#
class NullAgentContextException(InvalidAgentContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that AgentContext validation failed because the candidate was null.

    # PARENT:
        *   NullAgentContextException
        *   PlayerContextValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentContext validation failed: The candidate was null."