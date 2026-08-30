# src/domain/search/model/game/context.py

"""
Module: domain.search.model.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Game, Player, ModelContext


class ArenaContext(ModelContext[Arena]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a ArenaModelSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        game: Optional[Game]
        player: Optional[Player]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    player: Optional[Player] = None
    game: Optional[Game] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self.game,
            "player": self.player,
        }
