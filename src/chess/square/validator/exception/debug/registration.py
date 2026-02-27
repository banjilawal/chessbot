# src/chess/square/validator/exception/registration/player.py

"""
Module: chess.square.validator.exception.registration.player
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.square import SquareDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "SquareNotRegisteredBoardException",
]


# ======================# SQUARE_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class SquareNotRegisteredBoardException(SquareDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

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