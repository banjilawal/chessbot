# src/domain/search/stack/board/context.py

"""
Module: domain.search.stack.board
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Board, StackSearchContext, Team


class BoardSearchContext(StackSearchContext[Board]):
    """
    Role:
        -   Selection
        -   Routing mask

    Responsibilities:
        1.  Supply the criteria a BoardStackSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        team: Optional[Team]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        StackSearchContext
    """
    _arena: Optional[Arena] = None
    _team: Optional[Team] = None
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            team: Optional[Team] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            arena: Optional[Arena]
            team: Optional[Team]
        """
        super().__init__(id=id)
        self._arena = arena
        self._team = team
        
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "team": self._team,
        }
