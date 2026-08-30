# src/domain/search/model/maneuver/context.py

"""
Module: domain.search.model.maneuver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Maneuver, Player, ManeuverWinner, ModelContext


class ManeuverSearchContext(ModelContext[Maneuver]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a ManeuverModelSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        player: Optional[Player]
        winner: Optional[ManeuverWinner]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelSearchContext
    """
    _id: Optional[int]
    _arena: Optional[Arena]
    _player: Optional[Player]
    _winner: Optional[ManeuverWinner]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            player: Optional[Player] | None = None,
            winner: Optional[ManeuverWinner] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            arena: Optional[Arena]
            player: Optional[Player]
            winner: Optional[ManeuverWinner]
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
    def winner(self) -> Optional[ManeuverWinner]:
        return self._winner
        
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "player": self._player,
            "winner": self._winner,
        }
