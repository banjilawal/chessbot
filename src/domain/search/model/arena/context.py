# src/domain/search/model/arena/context.py

"""
Module: domain.search.model.arena.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from config import GameColor
from domain import Arena, Board, Game, Player, ModelContext


class ArenaContext(ModelContext[Arena]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply ArenaSearcher with targeting criteria.

    Attributes:
        id: Optional[int]
        game: Optional[Game]
        board: Optional[Board]
        player: Optional[Player]
        player_color: Optional[GameColor]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """

    _game: Optional[Game]
    _board: Optional[Board]
    _player: Optional[Player]
    _player_color: Optional[GameColor]
    
    def ___init__(
            self,
            id: Optional[int] | None = None,
            game: Optional[Game] | None = None,
            board: Optional[Board] | None = None,
            player: Optional[Player] | None = None,
            player_color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            game: Optional[Game]
            board: Optional[Board]
            player: Optional[Player]
            player_color: Optional[GameColor]
        """
        super().__init__(id=id)
        self._game = game
        self._board = board
        self._player = player
        self._player_color = player_color
        
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def player(self) -> Optional[Player]:
        return self._player
    
    @property
    def player_color(self) -> Optional[GameColor]:
        return self._player_color
    
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self._game,
            "player": self._player,
            "player_color": self._player_color,
        }
