# src/domain/search/context/persona/model/state.py

"""
Module: domain.search.context.persona.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain.model import Persona
from domain.model import Context


class PersonaContext(Context[Persona]):
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
        Context
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