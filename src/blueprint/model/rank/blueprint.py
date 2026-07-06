# src/blueprint/model/rank/blueprint.py

"""
Module: blueprint.model.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from model import Persona, Rank


@dataclass
class RankBlueprint(Blueprint[Rank]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Rank object.

    Attributes:
        id: Optional[int]
        persona: Persona

            
    Provides:

     Super Class:
        Blueprint
     """
    persona: Persona
    id: Optional[int] | None = None
