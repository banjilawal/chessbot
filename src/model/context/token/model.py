# src/model/context/token/model.py

"""
Module: model.context.token.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from model import Context, Coord, Rank, Team, Token
from system import GameColor


@dataclass
class TokenContext(Context[Token]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Token attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    rank: Optional[Rank]
    team: Optional[Team]
    ransom: Optional[int]
    color: Optional[GameColor]
    designation: Optional[str]
    current_position:Optional[Coord]
    opening_square_name: Optional[str]

    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "team": self.team,
            "rank": self.rank,
            "color": self.color,
            "ransom": self.ransom,
            "designation": self.designation,
            "current_position": self.current_position,
            "opening_square_name_name": self.opening_square_name
        }