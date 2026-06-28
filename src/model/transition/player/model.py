# src/model/event/player/model.py

"""
Module: model.event.player.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import EventTransition, Game, Player, Team


class PlayerEventTransition(EventTransition[Player]):
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
        EventTransition
    """
    id: Optional[id] = None
    name: Optional[str] = None
    team: Optional[Team] = None
    game: Optional[Game] = None
    class_name: Optional[str] = None
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "team": self.team,
            "game": self.game,
            "class_name": self.class_name,
        }
    