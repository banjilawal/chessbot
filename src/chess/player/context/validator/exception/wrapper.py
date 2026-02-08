# src/chess/owner/validator/exception/base.py

"""
Module: chess.owner.validator.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.player import PlayerContextException
from chess.system import ValidationFailedException

__all__ = [
    # ======================# PLAYER_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
    "PlayerContextValidationFailedException",
]


# ======================# PLAYER_CONTEXT_VALIDATION_FAILURE EXCEPTION #======================#
class PlayerContextValidationFailedException(PlayerContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a candidate failed its validation as a PlayerContext. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   AgentContextException
        *   ValidationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_FAILURE"
    DEFAULT_MESSAGE = "AgentContext validation failed."