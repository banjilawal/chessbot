# src/domain/search/context/stack/game/context.py.py

"""
Module: domain.search.context.stack.game.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from domain import Arena, Context, Game, Player, Square


class GameContext(Context[Game]):
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
        Context
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
