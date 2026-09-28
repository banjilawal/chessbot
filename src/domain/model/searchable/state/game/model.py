# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from typing import List, Optional

from domain import Arena, Championship, GamePlayerColorBinder, GameState, CheckmateAttack, Player, StateModel
from game import GameResult
from util import IdFactory


class Game(StateModel):
    """
     Role:
         - Data Holder

     Responsibilities:
        2.  Hold the game's state while its being played.

     Attributes:
        id: int
        arena: Arena
        white_player: Player
        black_player: Player
        binder_id: Optional[int]
        state: Optional[GameState]
        result: Optional[GameResult]

     Provides:

     Super Class:
        Model
     """
    _id: int
    _arena: Arena
    _state: GameState
    _result: Optional[GameResult]
    _binder: GamePlayerColorBinder
    _temp_binder_id: int
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            white_player: Player,
            black_player: Player,
            binder_id: Optional[int] | None = None,
            state: Optional[GameState] | None = None,
            result: Optional[GameResult] | None = None,
    ):
        """
        Args:
            id: int
            arena: Arena
            white_player: Player
            black_player: Player
            binder_id: Optional[int]
            state: Optional[GameState]
            result: Optional[GameResult]
        """
        super().__init__(id=id)
        self._arena = arena
        self._result = result
        self._state = state or GameState.NEW
        self._temp_binder_id = (
                binder_id or
                IdFactory.next_id(class_name="GamePlayerColorBinder")
        )
        
        self._binder = GamePlayerColorBinder(
            primary=self,
            id=self._temp_binder_id,
            white_player=white_player,
            black_player=black_player,
        )
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def binder(self) -> GamePlayerColorBinder:
        return self._binder
    
    @property
    def state(self) -> GameState:
        return self._state
    
    @state.setter
    def state(self, other: GameState):
        self._state = other
    
    @property
    def result(self) -> Optional[GameResult]:
        return self._result
    
    @result.setter
    def result(self, other:GameResult):
        self._result = other
        
    @property
    def binder_id(self) -> int:
        return self._binder.id
    
    @property
    def is_ready(self) -> bool:
        return self._state == GameState.READY
    
    @property
    def is_not_ready(self) -> bool:
        return not self.is_ready
    
    @property
    def is_running(self) -> bool:
        return self._state == GameState.STARTED
    
    @property
    def is_finished(self) -> bool:
        return (
                self._state == GameState.WON or
                self._state == GameState.TIED or
                self._state == GameState.CANCELLED
        )
    
    def __eq__(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Game):
            return self.id == other.id
        return False
    
    def __hash__(self) -> int:
        return super().__hash__(self)
