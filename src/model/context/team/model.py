# src/model/context/team/model.py

"""
Module: model.context.team.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from model import Board, Context, Player, Schema, Team
from system import GameColor


class TeamContext(Context[Team]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Team attribute-value search filter.

    Attributes:
            id: Optional[int]
            board: Optional[Board]
            player: Optional[Player]
            color: Optional[GameColor]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    board: Optional[Board] = None
    player: Optional[Player] = None
    color: Optional[GameColor] = None
    schema: Optional[Schema] = None
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self.board,
            "owner": self.player,
            "color": self.color,
            "schema": self.schema,
        }
