# src/context/game/model/state.py

"""
Module: context.game.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Dict, Optional

from model import CombatantToken, Hostage, Context, Game, Player, Square, Token


class HostageContext(Context[Hostage]):
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
    id: Optional[int] = None
    victor: Optional[Token] = None
    prisoner: Optional[CombatantToken] = None
    captured_square: Optional[Square] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "game": self.victor,
            "player": self.prisoner,
            "captured_square": self.captured_square,
        }
