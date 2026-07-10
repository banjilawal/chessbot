# src/operand/state/event/persona/operand/state.py

"""
Module: operand.state.event.persona.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from operand.catalog import Persona
from operand import EventTransition


class PersonaEventTransition(EventTransition[Persona]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Persona attribute-value tuple which selects an execution path.

    Attributes:
        name: Optional[str]
        quota: Optional[int]
        ransom: Optional[int]
        designation: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        EventTransition
    """
    name: Optional[str]
    quota: Optional[int]
    ransom: Optional[int]
    designation: Optional[str]

    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "ransom": self.ransom,
            "quota": self.quota,
            "designation": self.designation,
        }