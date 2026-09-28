# src/domain/binder/player/binder.py

"""
Module: domain.binder.player.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List

from config import GameColor
from domain import Archetype, ColorBinder, Player


class PlayerColorBinder(ColorBinder[Player]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Use GameColor to map Player to Archetype.
        
    Attributes:
        white_player: Player
        black_player: Player
        
    Provides:
        players_are_same: bool
        players_differ: bool
        to_dict: Dict[GameColor, Dict[Archetype, Player]]
        
    Super Class:
       ColorBinder
    """
    _entry: Dict[GameColor, Dict[Archetype, Player]]
    
    def __init__(
            self,
            white_player: Player,
            black_player: Player,
    ):
        """
        Args:
            white_player: Player
            black_player: Player
        """
        super().__init__()
        self._entry = {
            GameColor.WHITE: {Archetype.WHITE: white_player},
            GameColor.BLACK: {Archetype.BLACK: black_player},
        }
    
    @property
    def white_player(self) -> Player:
        return self._entry[GameColor.WHITE][Archetype.WHITE]
    
    @property
    def black_player(self) -> Player:
        return self._entry[GameColor.BLACK][Archetype.BLACK]
    
    @property
    def players(self) -> List[Player]:
        return [self.white_player, self.black_player]
    
    @property
    def players_are_same(self) -> bool:
        return self.white_player == self.black_player
    
    @property
    def players_differ(self) -> bool:
        return not self.players_are_same
    
    @property
    def items_are_different(self) -> bool:
        return self.players_differ
    
    @property
    def same_items(self) -> bool:
        return self.players_are_same
    
    @property
    def to_dict(self) -> Dict[GameColor, Dict[Archetype, Player]]:
        return self._entry
        
    