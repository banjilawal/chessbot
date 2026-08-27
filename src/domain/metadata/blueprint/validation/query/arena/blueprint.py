# src/domain/metadata/blueprint/validation/arena/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from domain.metadata.blueprint import QueryValidationBlueprint
from err import ArenaNullException
from domain.model import Arena, Game, Player
from config.setting import GameColor


@dataclass
class ArenaQueryValidationBlueprint(QueryValidationBlueprint[Arena]):
    id: Optional[int] = None
    name: Optional[str] = None
    player: Optional[Player] = None
    game: Optional[Game] = None
    color: Optional[GameColor] = None
    null_exception = ArenaNullException()
    model_type = Arena
