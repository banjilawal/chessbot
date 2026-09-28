# src/game/outcome/__init__.py

"""
Module: game.outcome.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Game


class GameOutcome(ABC):
    """
    Role:

    Responsibilities:
        1.  Determines how a Token can move.
        2.  How many points its worth.

    Attributes:
        id: int
        game: Game

    Provides:

    Super Class:
    """
    _id: int
    _game: Game
    
    def __init__(self, id: int, game: Game):
        self._id = id
        self._game = game
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def game(self) -> Game:
        return self._game
    