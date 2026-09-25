# src/domain/metadata/blueprint/model/state/game/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Arena, Game, GameState, Player, StateModelBlueprint
from err import GameNullException
from game import GameResult


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
        search_context_class: Type[GameContext]
        domain_null_exception: GameNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _id: int
    _arena: Arena
    _state: GameState
    _result: GameResult
    _white_player: Player
    _black_player: Player
    _binder_id: int

    def __init__(
            self,
            arena: Arena,
            binder_id: int,
            result: GameResult,
            white_player: Player,
            black_player: Player,
            state: Optional[GameState] | None = None,
            domain_class: Optional[Type[Game]] | None = None,
            domain_null_exception: Optional[GameNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            arena: Arena
            binder_id: int
            result: GameResult
            white_player: Player
            black_player: Player
            state: Optional[GameState]
            domain_class: Optional[Type[Game]]
            domain_null_exception: Optional[GameNullException]
            binder_id: Optional[int]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Game],
            domain_null_exception=domain_null_exception or GameNullException(),
        )
        self._arena = arena
        self._result = result
        self._binder_id = binder_id
        self._white_player = white_player
        self._black_player = black_player
        self._state = state or GameState.NEW
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def result(self) -> GameResult:
        return self._result
    
    @property
    def binder_id(self) -> Optional[int]:
        return self._binder_id
    
    @property
    def white_player(self) -> Player:
        return self._white_player
    
    @property
    def black_player(self) -> Player:
        return self._black_player
    
    @property
    def state(self) -> GameState:
        return self._state
    
    @property
    def domain_class(self) -> Type[Game]:
        return cast(Type[Game], super().domain_class)
    
    @property
    def domain_null_exception(self) -> GameNullException:
        return cast(GameNullException, super().domain_null_exception)

