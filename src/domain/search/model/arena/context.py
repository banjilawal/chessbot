# src/domain/search/stack/game/context.py

"""
Module: domain.search.stack.game
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Game, Player, ModelSearchContext


class ArenaSearchContext(ModelSearchContext[Arena]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a ArenaStackSearcher uses to find a hit.

    Attributes:
        id: Optional[int]
        game: Optional[Game]
        player: Optional[Player]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        StackSearchContext
    """
    player: Optional[Player] = None
    game: Optional[Game] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self.game,
            "player": self.player,
        }
