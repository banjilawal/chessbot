# src/model/context/arena/model.py

"""
Module: model.context.arena.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Arena, Arena, Context, Team


class ArenaContext(Context[Arena]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Arena attribute-value search filter.

    Attributes:
        id: Optional[int]
        arena: Optional[Arena]
        team: Optional[Team]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    arena: Optional[Arena] = None
    team: Optional[Team] = None
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "arena": self.arena,
            "team": self.team,
        }
