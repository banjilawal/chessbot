# src/domain/search/context/stack/game/context.py.py

"""
Module: domain.search.context.stack.game.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Arena, Game, Player, StackSearchContext


class ArenaSearchContext(StackSearchContext[Arena]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Game attribute-value search filter.

    Attributes:
        id: Optional[int]
        game: Optional[Game]
        player: Optional[Player]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    player: Optional[Player] = None
    game: Optional[Game] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self.game,
            "player": self.player,
        }
