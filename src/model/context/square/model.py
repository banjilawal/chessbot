# src/model/context/square/model.py

"""
Module: model.context.square.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from model import Board, Context, Coord, Square, SquareCategory, SquareState, Token


@dataclass
class SquareContext(Context[Square]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Square attribute-value tuple which selects an execution path.

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
        Context
    """
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    square_type: Optional[SquareCategory] = None
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "board": self.board,
            "coord": self.coord,
            "occupant": self.occupant,
            "state": self.state,
            "square_type": self.square_type,
        }