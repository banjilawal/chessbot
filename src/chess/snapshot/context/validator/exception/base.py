# src/chess/game/snapshot/context/validator/exception/exception.py

"""
Module: chess.game.snapshot.context.validator.exception.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from chess.game import GameSnapshotContextException
from chess.system import ValidationFailedException


__all__ = [
    # ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
    "InvalidGameSnapshotContextException",
]


# ======================# AGENT_CONTEXT VALIDATION SUPER CLASS #======================#
class InvalidGameSnapshotContextException(GameSnapshotContextException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised GameSnapshotContext validation.
    2.  Wraps unhandled exception that hit the finally-block in GameSnapshotContextValidator methods.

    # PARENT:
        *   GameSnapshotContextException
        *   ValidationFailedException

    # PROVIDES:
    InvalidGameSnapshotContextException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GameSnapshotContext validation failed."