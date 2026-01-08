# src/chess/player/validator/exception/null.py

"""
Module: chess.player.validator.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.agent import InvalidAgentException

__all__ = [
    #======================# PLAYER NULL EXCEPTION #======================#
    "NullAgentException",
]

#======================# PLAYER_CONTEXT NULL EXCEPTION #======================#
class NullAgentException(InvalidAgentException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an Player  but got null instead.

    # PARENT:
        *   PlayerValidationFailedException
        *   NullException

    # PROVIDES:
        *   NullAgentCException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_AGENT_ERROR"
    DEFAULT_MESSAGE = "Player cannot be null."
