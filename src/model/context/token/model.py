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

from err import TokenContextNullException
from model import Context, Coord, OpeningSquare, Rank, Team, Token
from setting import GameColor

@dataclass
class TokenContext(Context[Token]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Token attribute-value search filter.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square: Optional[OpeningSquare]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    id: Optional[int] | None = None
    rank: Optional[Rank] | None = None
    team: Optional[Team] | None = None
    ransom: Optional[int] | None = None
    color: Optional[GameColor] | None = None
    designation: Optional[str] | None = None
    current_position:Optional[Coord] | None = None
    opening_square: Optional[OpeningSquare] | None = None
    
    # def __init__(
    #         self,
    #     rank: Optional[Rank] | None = None,
    #     team: Optional[Team] | None = None,
    #     ransom: Optional[int] | None = None,
    #     color: Optional[GameColor] | None = None,
    #     designation: Optional[str] | None = None,
    #     current_position: Optional[Coord] | None = None,
    #     opening_square: Optional[OpeningSquare] | None = None,
    # ):

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
            "opening_squaree": self.opening_square
        }