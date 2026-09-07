# src/domain/metadata/blueprint/model/searchable/state/player/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Player,  StateModelBlueprint
from err import PlayerNullException
from game import GameAdviser





class PlayerBlueprint(StateModelBlueprint[Player]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a Player object.

    Attributes:
        name: str
        adviser: Optional[GameAdviser]
        id: Optional[int]
        
        domain_class: Type[Player]
        search_context_class: Type[PlayerContext]
        domain_null_exception: PlayerNullException

    Provides:

     Super Class:
        StateModelBlueprint
     """
    _name: str
    _adviser: Optional[GameAdviser]
    
    def __init__(self,
            name: str,
            adviser: Optional[GameAdviser] | None = None,
            domain_class: Optional[Type[Player]] | None = None,
            domain_null_exception: Optional[PlayerNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            name: str
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
        self._name = name
        self._adviser = adviser
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def adviser(self) -> Optional[GameAdviser]:
        return self._adviser

    @property
    def domain_class(self) -> Type[Player]:
        return cast(Type[Player], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PlayerNullException:
        return cast(PlayerNullException, super().domain_null_exception)