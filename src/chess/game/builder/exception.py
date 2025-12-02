# src/chess/game/builder/exception.py

"""
Module: chess.game.builder.exception
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.game import GameException
from chess.system import BuildFailedException

__all__ =  [
    # ======================# GAME BUILD EXCEPTIONS #======================#
    "GameBuildFailedException",
]

# ======================# GAME BUILD EXCEPTIONS #======================#
class GameBuildFailedException(GameException, BuildFailedException):
    """
    Catchall/wrapper exception for when a condition not handled directly by GameBuilder
    prevents successful Game creation.
    """
    ERROR_CODE = "GAME_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Game build failed."