# src/model/event/square/model.py

"""
Module: model.event.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from model import Board, EventTransition, Coord, Formation, Square, SquareState, Token


@dataclass
class SquareEventTransition(EventTransition[Square]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value search filter.

    Attributes:
            id: Optional[int]
            name: Optional[str]
            board: Optional[Board]
            coord: Optional[Coord]
            occupant: Optional[Token]
            state: Optional[SquareState]
            
    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    id: Optional[int] = None
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    formation: Optional[Formation] = None
    
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self.board,
            "coord": self.coord,
            "occupant": self.occupant,
            "state": self.state,
            "formation": self.formation,
        }