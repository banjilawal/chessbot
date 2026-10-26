# src/domain/context/model/player/context.py

"""
Module: domain.context.model.player.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Account, Archetype, Game, Player, PlayerType, Context, Team


class PlayerContext(Context[Player]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply PlayerSearcher with targeting criteria.

    Attributes:
        id: Optional[id]
        account: Optional[Account]
        game: Optional[Game]
        archetype: Option[Archetype]
        losses: Optional[Archetype]
        current_team: Optional[Team]
        player_type: Optional[PlayerCategory]

    Provides:
        -   def to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _id: Optional[int]
    _account: Optional[Account]
    _game: Optional[Game]
    _archetype: Optional[Archetype]
    _player_type: Optional[PlayerType]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            account: Optional[Account] | None = None,
            game: Optional[Game] | None = None,
            archetype: Optional[Archetype] | None = None,
            player_type: Optional[PlayerType] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            account: Optional[Account]
            game: Optional[Game]
            archetype: Optional[Archetype]
            player_type: Optional[PlayerCategory]
        """
        super().__init__(id=id)
        self._account = account
        self._game = game
        self._archetype = archetype
        self._player_type = player_type
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def archetype(self) -> Optional[Archetype]:
        return self._archetype
    
    @property
    def account(self) -> Optional[Account]:
        return self._account
    
    @property
    def player_type(self) -> Optional[PlayerType]:
        return self._player_type
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "account": self.account,
            "game": self._game,
            "archetype": self._archetype,
            "player_type": self._player_type,
        }
    