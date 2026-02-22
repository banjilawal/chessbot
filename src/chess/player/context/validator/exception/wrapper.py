# src/chess/owner/validator/exception/base.py

"""
Module: chess.owner.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.player import PlayerContextException
from chess.system import ValidationException

__all__ = [
    # ======================# PLAYER_CONTEXT_VALIDATION_FAILURE #======================#
    "PlayerContextValidationException",
]


# ======================# PLAYER_CONTEXT_VALIDATION_FAILURE #======================#
class PlayerContextValidationException(PlayerContextException, ValidationException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a PlayerContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   AgentContextException
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "AgentContext validation failed."