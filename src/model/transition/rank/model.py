# src/model/event/rank/model.py

"""
Module: model.event.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict

from model import EventTransition, Persona, Rank


class RankEventTransition(EventTransition[Rank]):
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
        EventTransition
    """
    persona: Persona

    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "persona": Persona,
        }



