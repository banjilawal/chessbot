# src/chess/game/number_bounds_validator/exception/registration/game.py

"""
Module: chess.game.number_bounds_validator.exception.registration.game
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.game import GameRegistrationException


__all__ = [
    #======================# GAME REGISTRATION EXCEPTION #======================#
    "GameNotRegisteredWithGameException",
]




#======================# GAME_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class GameNotRegisteredWithGameException(GameRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Game has assigned itself to a Game instance, the Game has not
        registered the Game as one of its two participants.
    2.  Raised if the game.game == game but game not in game.players

    # PARENT:
        *   GameRegistrationException

    # PROVIDES:
    GameNotRegisteredWithGameException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = (
        "Game is not registered as one of the Game's participants. Only the Game "
        "side of the relationship is set."
    )