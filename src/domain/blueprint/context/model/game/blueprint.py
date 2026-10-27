# src/domain/bluprint/context/model/game/blueprint.py

"""
Module: domain.bluprint.context.model.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import Account, Arena, GameContext, GameState, ContextBlueprint, Player
from err import GameContextNullException


class GameContextBlueprint(ContextBlueprint[GameContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a GameContext.
         
     Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        player: Optional[Player]
        state: Optional[GameState]
        
        domain_class: Type[GameContext]
        domain_null_exception: GameContextNullException

     Provides:

     Super Class:
        ContextBlueprint
     """
    
    _arena: Optional[Arena]
    _player: Optional[Player]
    _validation_state: Optional[GameState]
    _account: Optional[Account]
    
    def __init__(
            self,
            domain_class: Optional[Type[GameContext]] | None = None,
            domain_null_exception: Optional[GameContextNullException] | None = None,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            player: Optional[Player] | None = None,
            validation_state: Optional[GameState] | None = None,
            account: Optional[Account] | None = None,
    ):
        """
        Args:
            arena: Optional[Arena]
            player: Optional[Player]
            validation_state: Optional[GameState]
            account: Optional[Account]
            domain_class: Type[GameContext]
            domain_null_exception: GameContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[GameContext],
            domain_null_exception=domain_null_exception or GameContextNullException(),
        )
        self._arena = arena
        self._player = player
        self._state = validation_state
        self._account = account
    
    @property
    def domain_class(self) -> Type[GameContext]:
        return cast(Type[GameContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> GameContextNullException:
        return  cast(GameContextNullException, super().domain_null_exception)

    @property
    def player(self) -> Optional[Player]:
        return self._player
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def validation_state(self) -> Optional[GameState]:
        return self._state
    
    @property
    def account(self) -> Optional[Account]:
        return self._account
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "player": self._player,
            "state": self._state,
            "account": self._account,
        }
    
    
    
    
    


