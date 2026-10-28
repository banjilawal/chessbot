# src/domain/struct/binder/player/binder.py

"""
Module: domain.struct.binder.player.binder
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from __future__ import annotations

from typing import Dict, List, cast

from domain import Account, Archetype, ArchetypeBinder, Game, Player


class PlayerBinder(ArchetypeBinder[Player]):
    """
    Role:
        - Mapper

    Responsibility:
        1.  Immutable data structure insuring uniqueness and consistency
            between a Game's players.
        
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
        super().__init__(white_entry=white_player, black_entry=black_player)
        self._entry = {
            white_player.archetype: white_player,
            black_player.archetype: black_player,
        }
        
    @property
    def white_player(self) -> Player:
        return cast(Player, super().white_entry)
    
    @property
    def black_player(self) -> Player:
        return cast(Player, super().black_entry)
    
    @property
    def white_entry(self) -> Player:
        return self.white_entry
    
    @property
    def black_entry(self) -> Player:
        return self.black_entry
    
    @property
    def size(self) -> int:
        return len(self.bindings)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def archetypes_are_the_same(self) -> bool:
        return self.white_entry.archetype == self.black_entry.archetype
    
    @property
    def archetypes_differ(self) -> bool:
        return not self.archetypes_are_the_same
    
    @property
    def is_balanced(self) -> bool:
        return (
                self is not None and
                super().is_balanced and
                self.entries_are_unique and
                self.archetypes_differ
        )
    
    @property
    def is_not_balanced(self) -> bool:
        return self.is_not_empty and not self.is_balanced
    
    @property
    def consistency_exists(self) -> bool:
        if self.is_empty:
            return True
        return (
                self.is_balanced and
                self.entries_are_unique and
                self._white_entry.archetype == Archetype.WHITE and
                self._black_entry.archetype == Archetype.BLACK
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def entries_are_unique(self) -> bool:
        return (
                self.archetypes_differ and
                self.white_player != self.black_player
        )
    
    @property
    def entries_are_not_unique(self) -> bool:
        return not self.entries_are_unique
    
    @property
    def to_list(self) -> List[Player]:
        return [self.white_player, self.black_player]
    
    @property
    def bindings(self) -> Dict[Archetype, Player]:
        return self._entry
    
    @property
    def to_dict(self) -> Dict[str, Player]:
        return {
            "white": self.white_entry,
            "black": self.black_entry
        }
    