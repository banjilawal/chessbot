# src/model/context/player/model.py

"""
Module: model.context.player.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Context, Game, Player, Team


class PlayerContext(Context[Player]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Player attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[id]
        name: Optional[str]
        team: Optional[Team]
        game: Optional[Game]
        class_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    _team: Optional[Team]
    _game: Optional[Game]
    _class_name: Optional[str]
    
    def __init__(
            self,
            id: Optional[id] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            class_name: Optional[str] = None,
    ):
        """
        Args:
            id: Optional[id]
            name: Optional[str]
            team: Optional[Team]
            game: Optional[Game]
            class_name: Optional[str]
        """
        super().__init__(id=id, name=name)
        self._team = team
        self._game = game
        self._class_name = class_name
        
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def class_name(self) -> Optional[str]:
        return self._class_name
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "team": self._team,
            "game": self._game,
            "class_name": self._class_name,
        }
    