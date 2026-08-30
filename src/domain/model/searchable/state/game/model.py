# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from typing import List, Optional

from domain import Arena, Championship, GameState, MateEnemyKing, Player, StateModel
from game import GameWin


class Game(StateModel):
    """
    Role:Controller

    Responsibilities:
    Interface players use to change the Arena's state.

    Super Class:
    None

    # PROVIDES:
    Game

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (Player)
        *   black_player (Player)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _arena: Arena
    _white_player: Player
    _black_player: Player
    _state: GameState
    _win: Optional[GameWin]
    
    
    def __init__(
            self,
            id: int,
            white_player: Player,
            black_player: Player,
            arena: Arena
    ):
        super().__init__(id=id)
        self._arena = arena
        self._state = GameState.NEW
        self._white_player = white_player
        self._black_player = black_player
        self._win = None
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def white_player(self) -> Player:
        return self._white_player
    
    @property
    def black_player(self) -> Player:
        return self._black_player
    
    @property
    def players(self) -> List[Player]:
        return [self._white_player, self._black_player]
    
    @property
    def state(self) -> GameState:
        return self._state
    
    @state.setter
    def state(self, other: GameState):
        self._state = other
    
    @property
    def win(self) -> Optional[GameWin]:
        return self._win
    
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
