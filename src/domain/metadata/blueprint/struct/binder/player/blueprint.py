# src/domain/metadata/blueprint/struct/binder/player.blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, List, Optional, Type

from domain import Archetype, BinderBlueprint, Player, PlayerBinder
from err import PlayerBinderNullException


class PlayerBinderBlueprint(BinderBlueprint[PlayerBinder]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a PlayerBinder.

     Attributes:
        white_player: Player
        black_player: Player
        domain_class: Optional[Type[PlayerBinder]]
        domain_null_exception: Optional[PlayerBinderNullException]

     ProvideT:

     Super class:
        BinderBlueprint
     """
    
    _white_player: Player
    _black_player: Player
    
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
            domain_class=domain_class or PlayerBinder,
            domain_null_exception=domain_null_exception or PlayerBinderNullException(),
        )
        self._white_player = white_player
        self._black_player = black_player
        
    @property
    def white_player(self) -> Player:
        return self._white_player
    
    @property
    def black_player(self) -> Player:
        return self._black_player
    
    @property
    def players_are_unique(self) -> bool:
        return self._white_player != self._black_player
    
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
    def archetypes_are_the_same(self) -> bool:
        return self._white_player.archetype == self._black_player.archetype
    
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
                self._white_player.archetype == Archetype.WHITE and
                self._black_player.archetype == Archetype.BLACK
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    @property
    def bindings(self) -> Dict[Archetype, Player]:
        return {
            self._white_player.archetype: self._white_player,
            self._black_player.archetype: self._black_player,
        }
    
    @property
    def to_list(self) -> List[Player]:
        return [self._white_player, self._black_player]
    
    @property
    def to_dict(self) -> Dict[str, Player]:
        return {
            "white": self._white_player,
            "black": self._black_player,
        }
    