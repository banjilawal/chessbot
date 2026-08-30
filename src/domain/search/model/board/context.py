# src/domain/search/model/board/context.py

"""
Module: domain.search.model.board.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from config import GameColor
from domain import Arena, Board, BoardState, ModelContext, Team


class BoardContext(ModelContext[Board]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply BoardSearcher with argeting criteria.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        arena: Optional[Arena]
        state: Optional[BoardState]
        team_color: Optional[GameColor]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """

    _team: Optional[Team]
    _arena: Optional[Arena]
    _state: Optional[BoardState]
    _team_color: Optional[GameColor]

    
    def __init__(
            self,
            id: Optional[int] | None = None,
            team: Optional[Team] | None = None,
            arena: Optional[Arena] | None = None,
            state: Optional[BoardState] | None  = None,
            team_color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            team: Optional[Team]
            arena: Optional[Arena]
            state: Optional[BoardState]
            team_color: Optional[GameColor]
        """
        super().__init__(id=id)
        self._team = team
        self._state = state
        self._arena = arena
        self._team_color = team_color
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
        
    @property
    def state(self) -> Optional[BoardState]:
        return self._state
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def team_color(self) -> Optional[GameColor]:
        return self._team_color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "team": self._team,
            "state": self._state,
            "arena": self._arena,
            "team_color": self._team_color
        }
