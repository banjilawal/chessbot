# src/context/team/context.py

"""
Module: context.team.context
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from context import Context
from model import Board, Player, Schema, Team
from setting import GameColor


class TeamContext(Context[Team]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Team attribute-value search filter.

    Attributes:
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            color: Optional[GameColor]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _board: Optional[Board] = None
    _owner: Optional[Player] = None
    _color: Optional[GameColor] = None
    _schema: Optional[Schema] = None
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            board: Optional[Board] | None = None,
            owner: Optional[Player] | None = None,
            color: Optional[GameColor] | None = None,
            schema: Optional[Schema] | None = None,
    ):
        """
        Args
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            color: Optional[GameColor]
            schema: Optional[Schema
        """
        super().__init__(id=id, name=None)
        self._board = board
        self._owner = owner
        self._color = color
        self._schema = schema
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def owner(self) -> Optional[Player]:
        return self._owner
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def schema(self) -> Optional[Schema]:
        return self._schema
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self.board,
            "owner": self.owner,
            "color": self.color,
            "schema": self.schema,
        }