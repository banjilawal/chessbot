# src/domain/metadata/blueprint/context/game/blueprint.py

"""
Module: domain.metadata.blueprint.context.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import GameStackContextNullException
from domain.model import Blueprint, Game, GameContext, Player


@dataclass
class GameContextBlueprint(Blueprint[GameContext]):
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = GameStackContextNullException()
    model_type = GameContext
