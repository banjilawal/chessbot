# src/domain/search/model/team/context.py

"""
Module: domain.search.model.team
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from config import GameColor
from domain import Archetype, Board, Player, ModelSearchContext, Team


class TeamSearchContext(ModelSearchContext[Team]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a TeamModelSearcher uses to find a hit.

    Attributes:
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            color: Optional[GameColor]
            archetype: Optional[Archetype]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelSearchContext
    """
    _board: Optional[Board] = None
    _owner: Optional[Player] = None
    _color: Optional[GameColor] = None
    _archetype: Optional[Archetype] = None
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            board: Optional[Board] | None = None,
            owner: Optional[Player] | None = None,
            color: Optional[GameColor] | None = None,
            archetype: Optional[Archetype] | None = None,
    ):
        """
        Args
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            color: Optional[GameColor]
            archetype: Optional[Archetype]
        """
        super().__init__(id=id, name=None)
        self._board = board
        self._owner = owner
        self._color = color
        self._archetype = archetype
    
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
    def archetype(self) -> Optional[Archetype]:
        return self._archetype
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self.board,
            "owner": self.owner,
            "color": self.color,
            "archetype": self.archetype,
        }