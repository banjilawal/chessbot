# src/domain/struct/binder/player/binder.py

"""
Module: domain.struct.binder.player.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict

from domain import Archetype, ArchetypeBinder, Player


class PlayerBinder(ArchetypeBinder[Player]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Use GameColor to map Player to Archetype.
        
    Attributes:
        white_player: Player
        black_player: Player
        to_dict: Dict[str, Player]
        
    Provides:
        
    Super Class:
       ArchetypeBinder
    """
    _entry: Dict[Archetype, Player]
    
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
            white_player.archetype: white_player,
            black_player.archetype: black_player,
        }
    
    @property
    def white_player(self) -> Player:
        return self._entry[Archetype.WHITE]
    
    @property
    def black_player(self) -> Player:
        return self._entry[Archetype.BLACK]
    
    @property
    def entries_are_unique(self) -> bool:
        return self.is_full and self.white_player != self.black_player
    
    @property
    def entries_are_not_unique(self) -> bool:
        return self.is_full and self.white_player == self.black_player
    
    @property
    def consistency_exists(self) -> bool:
        if super().is_not_consistent:
            return False
        if self.entries_are_not_unique:
            return False
        if self.white_player.archetype == Archetype.BLACK:
            return False
        if self.black_player.archetype == Archetype.WHITE:
            return False
        return True
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def to_dict(self) -> Dict[str, Player]:
        return {
            "white": self.white_player,
            "black": self.black_player,
        }
    