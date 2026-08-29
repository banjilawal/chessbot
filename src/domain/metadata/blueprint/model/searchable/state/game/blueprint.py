# src/domain/metadata/blueprint/model/searchable/state/game/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from domain import Arena, Attack, Game, GameSearchContext, StateModelBlueprint
from err import GameNullException


class GameBlueprint(StateModelBlueprint[Game]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Game object.

     Attributes:
        id: Optional[int]
        arena: Arena
        captures: List[Attack]
        
        domain_class: Type[Game]
        search_context_class: Type[GameSearchContext]
        domain_null_exception: GameNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _arena: Arena
    _captured_tokens: List[Attack]
    
    def __init__(
            self,
            arena: Arena,
            captured_tokens: List[Attack],
            domain_class: Optional[Type[Game]] | None = None,
            search_context_class: Optional[Type[GameSearchContext]] | None = None,
            domain_null_exception: Optional[GameNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Game]]
            search_context_class: Optional[Type[GameSearchContext]]
            domain_null_exception: Optional[GameNullException]
            id: Optional[int]
            arena: Arena
            captured_tokens: List[Attack]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Game],
            search_context_class=search_context_class or Type[GameSearchContext],
            domain_null_exception=domain_null_exception or GameNullException(),
        )
        self._arena = arena
        self._captured_tokens = captured_tokens
    
    @property
    def domain_class(self) -> Type[Game]:
        return cast(Type[Game], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[GameSearchContext]:
        return cast(Type[GameSearchContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> GameNullException:
        return cast(GameNullException, super().domain_null_exception)
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def captured_tokens(self) -> List[Attack]:
        return self._captured_tokens
    

