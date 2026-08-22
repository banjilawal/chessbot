# src/domain/search/context/stack/board/context.py.py

"""
Module: domain.search.context.stack.board.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Board, StackSearchContext


class BoardSearchContext(StackSearchContext[Board]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Board attribute-value search filter.

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
