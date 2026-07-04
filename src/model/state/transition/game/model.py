# src/model/state/event/game/model/state.py

"""
Module: model.state.event.game.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import Arena, CombatantToken, Game, EventTransition, Game, Player, Square, Token


class GameEventTransition(EventTransition[Game]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Game attribute-value search filter.

    Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        player: Optional[Player]
        winner: Optional[Player]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    id: Optional[int] = None
    arena: Optional[Arena] = None
    player: Optional[Player] = None
    winner: Optional[Square] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self.arena,
            "player": self.player,
            "winner": self.winner,
        }
