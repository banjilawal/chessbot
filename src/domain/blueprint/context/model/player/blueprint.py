# src/domain/bluprint/context/model/player/blueprint.py

"""
Module: domain.bluprint.context.model.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Account, Archetype, Arena, Game, ContextBlueprint, PlayerType, PlayerContext, Team
from err import PlayerContextNullException


class PlayerContextBlueprint(ContextBlueprint[PlayerContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an PlayerContext.
         
     Attributes:
        id: Optional[id]
        game: Optional[Game]
        arena: Optional[Arena]
        account: Optional[Account]
        player_type: Optional[Playertype]
        
        domain_class: Type[PlayerContext]
        domain_null_exception: PlayerContextNullException

     Provides:

     Super Class:
        ContextBlueprint
     """
    
    _id: Optional[int]
    _game: Optional[Game]
    _account: Optional[Account]
    _player_type: Optional[PlayerType]
    _archetype: Optional[Archetype]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            account: Optional[Account] | None = None,
            archetype: Optional[Archetype] | None = None,
            player_type: Optional[PlayerType] | None = None,
            domain_class: Optional[Type[PlayerContext]] | None = None,
            domain_null_exception: Optional[PlayerContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            game: Optional[Game]
            account: Optional[Account]
            player_type: Optional[PlayerType]
            domain_class: Type[PlayerContext]
            domain_null_exception: PlayerContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[PlayerContext],
            domain_null_exception=domain_null_exception or PlayerContextNullException(),
        )
        self._game = game
        self._archetype = archetype
        self._account = account
        self._player_type = player_type
    
    @property
    def domain_class(self) -> Type[PlayerContext]:
        return cast(Type[PlayerContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PlayerContextNullException:
        return  cast(PlayerContextNullException, super().domain_null_exception)
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def account(self) -> Optional[Account]:
        return self._account
    
    @property
    def archetype(self) -> Optional[Archetype]:
        return self._archetype
    
    @property
    def player_type(self) -> Optional[PlayerType]:
        return self._player_type
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self._game,
            "account": self._account,
            "archetype": self._archetype,
            "player_type": self._player_type,
        }
    
    
    
    
    


