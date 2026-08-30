# src/domain/search/model/game/context.py

"""
Module: domain.search.model.game.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from config import GameColor
from domain import Arena, Game, GameState, Player, ModelContext
from game import GameWin


class GameContext(ModelContext[Game]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply GameSearcher with targeting criteria.

    Attributes:
        id: Optional[int]
        win: Optional[GameWin]
        arena: Optional[Arena]
        player: Optional[Player]
        state: Optional[GameState]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    
    _id: Optional[int]
    _win: Optional[GameWin]
    _arena: Optional[Arena]
    _player: Optional[Player]
    _state: Optional[GameState]
    _player_color: Optional[GameColor]

    
    def __init__(
            self,
            id: Optional[int] | None = None,
            win: Optional[GameWin] | None = None,
            arena: Optional[Arena] | None = None,
            player: Optional[Player] | None = None,
            state: Optional[GameState] | None = None,
            player_color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            win: Optional[GameWin]
            arena: Optional[Arena]
            player: Optional[Player]
            state: Optional[GameState]
            player_color: Optional[GameColor]
        """
        super().__init__(id=id)
        self._win = win
        self._arena = arena
        self._player = player
        self._state = state
        self._player_color = player_color
        
    @property
    def win(self) -> Optional[GameWin]:
        return self._win
        
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def player(self) -> Optional[Player]:
        return self._player
    
    @property
    def state(self) -> Optional[GameState]:
        return self._state
    
    @property
    def player_color(self) -> Optional[GameColor]:
        return self._player_color
        
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "win": self._win,
            "arena": self._arena,
            "player": self._player,
            "state": self._state,
            "player_color": self._player_color
        }
