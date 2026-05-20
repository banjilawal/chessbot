# src/blueprint/rank/model.py

"""
Module: blueprint.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import RankNullException
from model import Blueprint, Persona, Rank

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
        model_type: Rank
        null_exception: RankNullException
            
    Provides:

     Super Class:
        Blueprint
     """
    persona: Persona
    id: Optional[int] | None = None
    null_exception: RankNullException = RankNullException()
    model_type: Rank = Rank
