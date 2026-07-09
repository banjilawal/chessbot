# src/blueprint/model/rank/blueprint.py

"""
Module: blueprint.model.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from blueprint import Blueprint
from err import RankNullException
from model import Rank
from schema import Persona


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
    """
    Args:
        persona: Persona
        null_exception: RankNullException
        owner: Rank
        owner_name: str
    """
    persona: Persona
    null_exception: RankNullException = RankNullException()
    owner: Rank = Type[Rank]
    owner_name: str = type(owner).__name__
