# src/domain/search/model/player/context.py

"""
Module: domain.search.model.player
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Game, Player, PlayerCategory, ModelContext, Team


class PlayerContext(ModelContext[Player]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a PlayerModelSearcher uses to find a hit.

    Attributes:
        id: Optional[id]
        name: Optional[str]
        team: Optional[Team]
        game: Optional[Game]
        player_category: Optional[str]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    _id: Optional[int]
    _name: Optional[str]
    _team: Optional[Team]
    _game: Optional[Game]
    _player_category: Optional[PlayerCategory]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            team: Optional[Team] | None = None,
            game: Optional[Game] | None = None,
            player_category: Optional[PlayerCategory] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            team: Optional[Team]
            game: Optional[Game]
            player_category: Optional[PlayerCategory]
        """
        super().__init__(id=id, name=name)
        self._team = team
        self._game = game
        self._player_category = player_category
        
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def player_category(self) -> Optional[PlayerCategory]:
        return self._player_category
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "team": self._team,
            "game": self._game,
            "player_category": self._player_category,
        }
    