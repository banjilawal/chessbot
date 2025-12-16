# src/chess/player_agent/validator/exception/null/exception.py

"""
Module: chess.player_agent.validator.exception.null.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentException

__all__ = [
    #======================# AGENT NULL EXCEPTIONS #======================#
    "NullAgentException",
]

#======================# AGENT_CONTEXT NULL EXCEPTIONS #======================#
class NullAgentException(InvalidAgentException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an PlayerAgent  but got null instead.

    # PARENT:
        *   InvalidAgentException
        *   NullException

    # PROVIDES:
        *   NullAgentCException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_ERROR"
    DEFAULT_MESSAGE = "PlayerAgent cannot be null."
