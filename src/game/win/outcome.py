# src/game/outcome/__init__.py

"""
Module: game.outcome.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from artifcat import CheckmateResult
from domain import Game, Player
from game import GameOutcome


class GameWin(GameOutcome):
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
        GameOutcome
    """
    _winner: Player
    _checkmate_result: CheckmateResult
    
    def __init__(self, id: int, game: Game, winner: Player, checkmate_result: CheckmateResult):
        super().__init_subclass__(id, game)
        self._winner = winner
        self._checkmate_result = checkmate_result
        
    @property
    def winner(self) -> Player:
        return self._winner
    
    @property
    def checkmate_result(self) -> CheckmateResult:
        return self._checkmate_result