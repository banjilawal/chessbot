# src/operand/state/event/coord/operand/state.py

"""
Module: operand.state.event.coord.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from operand import EventTransition, Coord


class CoordEventTransition(EventTransition[Coord]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Coord attribute-value search filter.

    Attributes:
            row: Optional[int]
            column: Optional[int]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    row: Optional[int] = None
    column: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "row": self.row,
            "column": self.column,
        }
