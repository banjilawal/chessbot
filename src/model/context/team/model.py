# src/model/context/team/model.py

"""
Module: model.context.team.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from model import Board, Context, Player, Team
from system import GameColor


class TeamContext(Context[Team]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Team attribute-value tuple which selects an execution path.

    Attributes:
            id: Optional[int]
            board: Optional[Board]
            player: Optional[Player]
            color: Optional[GameColor]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _board: Optional[Board] = None
    _player: Optional[Player] = None
    _color: Optional[GameColor] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            board: Optional[Board] = None,
            player: Optional[Player] = None,
            color: Optional[GameColor] = None,
    ):
        """
        Args:
            id: Optional[int]
            board: Optional[Board]
            player: Optional[Player]
            color: Optional[GameColor]
        """
        super().__init__(id=id, name=None)
        self._board = board
        self._player = player
        self._color = color
    
    @property
    def owner(self) -> Optional[Player]:
        return self._player
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self._board,
            "owner": self._player,
            "color": self._color,
        }
