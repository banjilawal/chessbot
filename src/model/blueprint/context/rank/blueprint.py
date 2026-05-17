# src/model/blueprint/context/rank/blueprint.py

"""
Module: model.blueprint.context.rank.blueprint
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
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = RankContextNullException()
    model_type = RankContext
    
