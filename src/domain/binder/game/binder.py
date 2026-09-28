# src/domain/binder/game/binder.py

"""
Module: domain.binder.game.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List, Optional, cast

from config import GameColor
from domain import ColorBinder, Game, Player


class PlayerColorBinder(ColorBinder[Player]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Maps the Player correctly to its color slot on the Game.
        
    Attributes:
        primary: Game
        white_player: Player
        black_player: Player
        
    Provides:
        
    Super Class:
       ColorBinder
    """
    _entry: Dict[GameColor, Player]
    
    def __init__(
            self,
            white_player: Player,
            black_player: Player,
            max_capacity: Optional[int] | None = None,
    ):
        """
        Args:
            white_player: Player
            black_player: Player
            max_capacity: Optional[int]
        """
        super().__init__(
            primary=primary, 
            max_capacity=max_capacity or self.MAX_CAPACITY,
        )
        self._entry = {
            GameColor.WHITE: white_player,
            GameColor.BLACK: black_player,
        }
    
    @property
    def white_player(self) -> Player:
        return self._entry[GameColor.WHITE]
    
    @property
    def black_player(self) -> Player:
        return self._entry[GameColor.BLACK]
    
    @property
    def players(self) -> List[Player]:
        return [self.white_player, self.black_player]
    
    @property
    def players_are_same(self) -> bool:
        return self.white_player == self.black_player
    
    @property
    def players_differ(self):
        return not self.players_are_same
    
    @property
    def to_dict(self) -> Dict[GameColor, Player]:
        return self._entry
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PlayerColorBinder):
            return self.id == other.id
        return False
        
    def __hash__(self):
        return hash(self.id)

        
    