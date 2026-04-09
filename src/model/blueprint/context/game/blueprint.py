# src/model/blueprint/context/game/blueprint.py

"""
Module: model.blueprint.context.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import GameContext, Blueprint, Game, Player


@dataclass
class GameContextBlueprint(Blueprint[GameContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
