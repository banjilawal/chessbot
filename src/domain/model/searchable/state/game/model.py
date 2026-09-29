# src/domain/model/searchable/state/game/model.py

"""
Module: domain.model.searchable.state.game.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from typing import Optional

from domain import (
    Arena, CheckmateEncounter, GameState, PlayerArchetypeBinder, StalemateEncounter,
    StateModel
)
from sync import TurnManagementService


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
        checkmate: Optional[CheckmateEncounter]
        stalemate: Optional[StalemateEncounter]

     Provides:

     Super Class:
        Model
     """
    _id: int
    _arena: Arena
    _state: GameState
    _binder: PlayerArchetypeBinder
    _turn_service: TurnManagementService
    _checkmate: Optional[CheckmateEncounter]
    _stalemate: Optional[StalemateEncounter]
    
    def __init__(
            self,
            id: int,
            arena: Arena,
            binder: PlayerArchetypeBinder,
            turn_service: Optional[TurnManagementService] | None = None,
    ):
        """
        Args:
            id: int
            arena: Arena
            binder: PlayerArchetypeBinder
            turn_service: Optional[TurnManagementService]
        """
        super().__init__(id=id)
        self._arena = arena
        self._binder = binder
        self._turn_service = turn_service
        self._checkmate = None
        self._stalemate = None

    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def binder(self) -> PlayerArchetypeBinder:
        return self._binder
    
    @property
    def turn_service(self) -> TurnManagementService:
        return self._turn_service
    
    @property
    def checkmate(self) -> Optional[CheckmateEncounter]:
        return self._checkmate
    
    @checkmate.setter
    def checkmate(self, other: CheckmateEncounter):
        self._checkmate = other
    
    @property
    def stalemate(self) -> Optional[StalemateEncounter]:
        return self.stalemate
    
    @stalemate.setter
    def stalemate(self, other: StalemateEncounter):
        self._stalemate = other
    
    @property
    def state(self) -> GameState:
        return self._state
    
    @state.setter
    def state(self, other: GameState):
        self._state = other
    
    @property
    def is_ready(self) -> bool:
        return (
                self._checkmate is None and
                self._stalemate is None and
                self._state == GameState.READY and
                self._arena.board.has_been_filled
        )
    
    @property
    def is_not_ready(self) -> bool:
        return not self.is_ready
    
    @property
    def is_running(self) -> bool:
        return (
                self._checkmate is None and
                self._stalemate is None and
                self._state == GameState.STARTED and
                self._arena.opening_move_launched
        )
    
    @property
    def is_not_running(self) -> bool:
        return self.is_finished or self.is_not_ready
    
    @property
    def is_won(self) -> bool:
        return (
                self._checkmate is not None and
                self._stalemate is None and
                self._state == GameState.WON and
                isinstance(self._checkmate, CheckmateEncounter)
        )
    
    @property
    def is_stalemated(self) -> bool:
        return (
            self._checkmate is None and
            self._stalemate is not None and
            self._state == GameState.STALEMATE and
            isinstance(self._stalemate, StalemateEncounter)
        )
    
    @property
    def is_cancelled(self) -> bool:
        return (
            self._checkmate is None and
            self._stalemate is None and
            self._state == GameState.CANCELLED
        )
    
    @property
    def is_finished(self) -> bool:
        return (
                self.is_won or
                self.is_stalemated or
                self.is_cancelled
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
