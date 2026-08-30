# src/domain/metadata/blueprint/context/model/game/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Arena, GameContext, ModelContextBlueprint, Player
from err import GameContextNullException


class GameContextBlueprint(ModelContextBlueprint[GameContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a GameContext.
         
     Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        player: Optional[Player]
        
        domain_class: Type[GameContext]
        domain_null_exception: GameContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """

    _arena: Optional[Arena]
    _player: Optional[Player]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            player: Optional[Player] | None = None,
            domain_class: Optional[Type[GameContext]] | None = None,
            domain_null_exception: Optional[GameContextNullException] | None = None,
    ):
        """
        Args:
            arena: Optional[Arena]
            player: Optional[Player]
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
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "player": self._player,
        }
    
    
    
    
    


