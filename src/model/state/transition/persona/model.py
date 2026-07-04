# src/model/state/event/persona/model/state.py

"""
Module: model.state.event.persona.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from model.catalog import Persona
from model import EventTransition


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