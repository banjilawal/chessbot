# src/operand/state/event/formation/operand/state.py

"""
Module: operand.state.event.formation.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from operand import Formation, EventTransition, Persona
from system import GameColor


class FormationEventTransition(EventTransition[Formation]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Formation attribute-value search filter.

    Attributes:
        id: Optional[int]
        formation: Optional[Formation]
        team: Optional[Team]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    persona: Optional[Persona] = None,
    square_name: Optional[str] = None,
    designation: Optional[str] = None,
    color: Optional[GameColor] = None,
    
    @property
    def to_dict(self) -> dict[str, Any]:
        return {
            "color": self.color,
            "persona": self.persona,
            "square_name": self.square_name,
            "designation": self.designation,
        }
