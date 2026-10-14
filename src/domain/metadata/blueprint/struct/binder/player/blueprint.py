# src/domain/metadata/blueprint/struct/binder/player.blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional, Type, cast

from domain import Archetype, BinderBlueprint, Player, PlayerBinder
from err import PlayerBinderNullException


class PlayerBinderBlueprint(BinderBlueprint[PlayerBinder]):
    """
     Role:
        1.  Metadata

     ResponsibilitieT:
         1.  Provide attributes for hydrating a PlayerBinder.

     AttributeT:
        white_player: Player
        black_player: Player
        domain_class: Optional[Type[PlayerBinder]]
        domain_null_exception: Optional[PlayerBinderNullException]

     ProvideT:

     Super class:
        BinderBlueprint
     """
    
    def __init__(
            self,
            white_player: Player,
            black_player: Player,
            domain_class: Optional[Type[PlayerBinder]] | None = None,
            domain_null_exception: Optional[PlayerBinderNullException] | None = None,
    ):
        """
        ArgT:
            white_player: Player
            black_player: Player
            domain_class: Optional[Type[PlayerBinder]]
            domain_null_exception: Optional[PlayerBinderNullException]
        """
        super().__init__(
            white_entry=white_player,
            black_entry=black_player,
            domain_class=domain_class or PlayerBinder,
            domain_null_exception=domain_null_exception or PlayerBinderNullException(),
        )
        
    @property
    def white_player(self) -> Player:
        return cast(Player, super().white_entry)
    
    @property
    def black_player(self) -> Player:
        return cast(Player, super().black_entry)
    
    @property
    def white_entry(self) -> Player:
        return self.white_player
    
    @property
    def black_entry(self) -> Player:
        return self.black_player
    
    @property
    def players_are_unique(self) -> bool:
        return self.white_player != self.black_player
    
    @property
    def players_are_not_unique(self) -> bool:
        return not self.players_are_unique
    
    @property
    def entries_are_unique(self) -> bool:
        return self.players_are_unique
    
    @property
    def entries_are_not_unique(self) -> bool:
        return not self.entries_are_unique
    
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
        return not self.is_balanced
    
    @property
    def consistency_exists(self) -> bool:
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
    def bindings(self) -> Dict[Archetype, Player]:
        return {
            self.white_player.archetype: self.white_player,
            self.black_player.archetype: self.black_player,
        }
    
    @property
    def to_dict(self) -> Dict[str, Player]:
        return {
            "white": self.white_player,
            "black": self.black_player,
        }
    