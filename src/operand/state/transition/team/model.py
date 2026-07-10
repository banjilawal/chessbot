# src/operand/state/event/team/operand/state.py

"""
Module: operand.state.event.team.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from operand import Board, EventTransition, Player, Schema, Team
from setting import GameColor


class TeamEventTransition(EventTransition[Team]):
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
            owner: Optional[Player]
            color: Optional[GameColor]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    board: Optional[Board] = None
    owner: Optional[Player] = None
    color: Optional[GameColor] = None
    schema: Optional[Schema] = None
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self.board,
            "owner": self.owner,
            "color": self.color,
            "schema": self.schema,
        }
