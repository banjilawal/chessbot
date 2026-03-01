# src/logic/square/validator/exception/registration/player.py

"""
Module: logic.square.validator.exception.registration.player
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from logic.square import SquareDebugException
from logic.system import NotRegisteredException

__all__ = [
    # ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "SquareNotRegisteredBoardException",
]


# ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class SquareNotRegisteredBoardException(SquareDebugException, NotRegisteredException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the candidate square had not registered with its board.

    # PARENT:
        *   SquareDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_NOT_REGISTERED_WITH_BOARD_EXCEPTION"
    MSG = "Square validation failed: The candidate square had not registered with its board."