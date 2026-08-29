# src/domain/search/model/game/context.py

"""
Module: domain.search.model.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Game, Player, GameWinner, ModelSearchContext


class GameSearchContext(ModelSearchContext[Game]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a GameModelSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        player: Optional[Player]
        winner: Optional[GameWinner]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelSearchContext
    """
    _id: Optional[int]
    _arena: Optional[Arena]
    _player: Optional[Player]
    _winner: Optional[GameWinner]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            player: Optional[Player] | None = None,
            winner: Optional[GameWinner] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            arena: Optional[Arena]
            player: Optional[Player]
            winner: Optional[GameWinner]
        """
        super().__init__(id=id)
        self._arena = arena
        self._player = player
        self._winner = winner
        
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def player(self) -> Optional[Player]:
        return self._player
    
    @property
    def winner(self) -> Optional[GameWinner]:
        return self._winner
        
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "player": self._player,
            "winner": self._winner,
        }
