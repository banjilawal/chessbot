# src/domain/search/model/player/context.py

"""
Module: domain.search.model.player.context
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
        1.  Supply PlayerSearcher with targeting criteria.

    Attributes:
        id: Optional[id]
        name: Optional[str]
        game: Optional[Game]
        wins: Option[bool]
        losses: Optional[bool]
        current_team: Optional[Team]
        player_category: Optional[PlayerCategory]

    Provides:
        -  def to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    _id: Optional[int]
    _name: Optional[str]
    _game: Optional[Game]
    _wins: Optional[bool]
    _losses: Optional[bool]
    _current_team: Optional[Team]
    _player_category: Optional[PlayerCategory]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            game: Optional[Game] | None = None,
            wins: Optional[bool] | None = None,
            losses: Optional[bool] | None = None,
            current_team: Optional[Team] | None = None,
            player_category: Optional[PlayerCategory] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            team: Optional[Team]
            game: Optional[Game]
            wins: Optional[bool]
            losses: Optional[bool]
            current_team: Optional[Team]
            player_category: Optional[PlayerCategory]
        """
        super().__init__(id=id, name=name)
        self._game = game
        self._wins = wins
        self._losses = losses
        self._current_team = current_team
        self._player_category = player_category
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def wins(self) -> Optional[bool]:
        return self._wins
    
    @property
    def losses(self) -> Optional[bool]:
        return self._losses
    
    @property
    def current_team(self) -> Optional[Team]:
        return self._current_team
    
    @property
    def player_category(self) -> Optional[PlayerCategory]:
        return self._player_category
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "game": self._game,
            "wins": self._wins,
            "losses": self._losses,
            "current_team": self._current_team,
            "player_category": self._player_category,
        }
    