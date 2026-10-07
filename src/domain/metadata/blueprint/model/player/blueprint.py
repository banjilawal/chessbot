# src/domain/metadata/blueprint/model/player/blueprint.py

"""
Module: domain.metadata.blueprint.model.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Account, Archetype, Game, ModelBlueprint, Player
from err import PlayerNullException
from sync import GameAdviser


class PlayerBlueprint(ModelBlueprint[Player]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Player object.

    Attributes:
        game: Game
        account: Account
        archetype: Archetype
        adviser: Optional[GameAdviser]
        id: Optional[int]
        
        domain_class: Type[Player]
        domain_null_exception: PlayerNullException

    Provides:

     Super Class:
        ModelBlueprint
     """
    _game: Game
    _account: Account
    _archetype: Archetype
    _adviser: Optional[GameAdviser]
    
    def __init__(self,
            game: Game,
            account: Account,
            archetype: Archetype,
            adviser: Optional[GameAdviser] | None = None,
            domain_class: Optional[Type[Player]] | None = None,
            domain_null_exception: Optional[PlayerNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            game: Game
            account: Account
            archetype: Archetype
            adviser: Optional[GameAdviser]
            domain_class: Optional[Type[Player]]
            domain_null_exception: Optional[PlayerNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Player],
            domain_null_exception=domain_null_exception or PlayerNullException(),
        )
        self._game = game
        self._account = account
        self._archetype = archetype
        self._adviser = adviser
    
    @property
    def account(self) -> Account:
        return self._account
    
    @property
    def archetype(self) -> Archetype:
        return self._archetype
    
    @property
    def game(self) -> Game:
        return self._game
    
    @property
    def adviser(self) -> Optional[GameAdviser]:
        return self._adviser
    
    @property
    def domain_class(self) -> Type[Player]:
        return cast(Type[Player], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PlayerNullException:
        return cast(PlayerNullException, super().domain_null_exception)