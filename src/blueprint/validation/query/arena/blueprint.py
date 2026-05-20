# src/blueprint/validation/arena/blueprint.py

"""
Module: blueprint.validation.query.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from err import ArenaNullException
from model import Arena, Blueprint, Game, Player
from setting import GameColor


@dataclass
class ArenaQueryValidationBlueprint(QueryValidationBlueprint[Arena]):
    id: Optional[int] = None
    name: Optional[str] = None
    player: Optional[Player] = None
    game: Optional[Game] = None
    color: Optional[GameColor] = None
    null_exception = ArenaNullException()
    model_type = ArenaValidation
