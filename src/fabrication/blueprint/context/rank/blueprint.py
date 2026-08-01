# src/blueprint/context/rank/blueprint.py

"""
Module: blueprint.context.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import RankContextNullException
from model import RankContext, Blueprint, Game, Player


@dataclass
class RankContextBlueprint(Blueprint[RankContext]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a RankContext instance.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        player: Optional[Player]
        game: Optional[Game]
        null_exception = RankContextNullException
        model_type = RankContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = RankContextNullException()
    model_type = RankContext
    
