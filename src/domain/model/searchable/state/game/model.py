# src/domain/model/searchable/state/arena/model.py

"""
Module: domain.model.searchable.state.arena.model
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

from typing import List, Optional

from domain import Arena, GameState, MateEnemyKing, Player, StateModel


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
    
    
    def __init__(
            self,
            id: int,
            white_player: Player,
            black_player: Player,
            arena: Arena
    ):
        super().__init__()
        self._id = id
        self._arena = arena
        self._state = GameState.NEW
        self._white_player = white_player
        self._black_player = black_player

    
    @property
    def id(self) -> int:
        return self._id
    
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
    def check_mate(self) -> Optional[MateEnemyKing]:
        return None
