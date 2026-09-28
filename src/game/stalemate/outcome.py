# src/game/outcome/__init__.py

"""
Module: game.outcome.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from domain import CheckmateEncounter, Game, Player
from game import GameOutcome


class Stalemate(GameOutcome):
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
    _checkmate: CheckmateEncounter
    
    def __init__(
            checkmate: CheckmateEncounter
    ):
        super().__init_subclass__(id,)
        
        
    @property
    def game(self) -> Game:
        return self._checkmate.victor.team.board.arena.game
        
    @property
    def winner(self) -> Player:
        return self._checkmate.victor.team.owner
    
    @property
    def looser(self) -> Player:
        return self._checkmate.looser.team.owner
    
    @property
    def checkmate(self) -> CheckmateEncounter:
        return self._checkmate