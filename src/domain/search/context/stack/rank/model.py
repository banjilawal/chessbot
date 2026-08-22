# src/domain/search/context/stack/rank/context.py.py

"""
Module: domain.search.context.stack.rank.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict

from domain import Context, Persona, Rank


class RankContext(Context[Rank]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Rank attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        persona: Optional[Persona]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
    """
    persona: Persona

    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "persona": Persona,
        }



