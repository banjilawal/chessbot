# src/chess/game/validator/exception/registration/base.py

"""
Module: chess.game.validator.exception.registration.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import InvalidGameException
from chess.system import RegistrationException

__all__ = [
    # ======================# GAME REGISTRATION EXCEPTION SUPER CLASS #======================#
    "GameRegistrationException",
]


# ======================# GAME_REGISTRATION EXCEPTION SUPER CLASS #======================#
class GameRegistrationException(InvalidGameException, RegistrationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall Exception for when an Game has set its owner correctly but the owner does not
        have the game in its collection.

    # PARENT:
        *   InvalidGameException
        *   RegistrationException

    # PROVIDES:
    GameRegistrationException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Game not registered with parent."