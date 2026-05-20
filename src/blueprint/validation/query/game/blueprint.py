# src/blueprint/validation/game/blueprint.py

"""
Module: blueprint.validation.query.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import GameNullException
from model import Blueprint, Game, GameValidation, Player


@dataclass
class GameQueryValidationBlueprint(QueryValidationBlueprint[Game]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = GameNullException()
    model_type = GameValidation
