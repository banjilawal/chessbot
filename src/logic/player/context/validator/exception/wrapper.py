# src/logic/player/validator/exception/base.py

"""
Module: logic.player.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from logic.player import PlayerContextException
from logic.system import ValidationException

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
    ERR_CODE = "AGENT_CONTEXT_VALIDATION_FAILURE"
    MSG = "AgentContext validation failed."