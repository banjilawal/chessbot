# src/domain/search/model/team/context.py

"""
Module: domain.search.model.team.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from config import GameColor
from domain import Archetype, Board, GameState, Player, ModelContext, Team, TeamState


class TeamContext(ModelContext[Team]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply TeamSearcher with targeting criteria.

    Attributes:
        id: Optional[int]
        board: Optional[Board]
        owner: Optional[Player]
        state: Optional[TeamState]
        color: Optional[GameColor]
        archetype: Optional[Archetype]

    Provides:
        -  def to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    _board: Optional[Board]
    _owner: Optional[Player]
    _state: Optional[GameState]
    _color: Optional[GameColor]
    _archetype: Optional[Archetype]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            board: Optional[Board] | None = None,
            owner: Optional[Player] | None = None,
            state: Optional[GameState] | None = None,
            color: Optional[GameColor] | None = None,
            archetype: Optional[Archetype] | None = None,
    ):
        """
        Args
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            state: Optional[TeamState]
            color: Optional[GameColor]
            archetype: Optional[Archetype]
        """
        super().__init__(id=id, name=None)
        self._board = board
        self._owner = owner
        self._state = state
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
    def state(self) -> Optional[GameState]:
        return self._state
    
    @property
    def archetype(self) -> Optional[Archetype]:
        return self._archetype
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self._board,
            "owner": self._owner,
            "stat": self._state,
            "color": self._color,
            "archetype": self._archetype,
        }