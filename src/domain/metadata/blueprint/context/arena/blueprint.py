# src/domain/metadata/blueprint/context/arena/blueprint.py

"""
Module: domain.metadata.blueprint.context.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import ArenaStackContextNullException
from domain.model import ArenaContext, Blueprint, Game, Player
from config.setting import GameColor


@dataclass
class ArenaContextBlueprint(Blueprint[ArenaContext]):
    id: Optional[int] = None
    name: Optional[str] = None
    player: Optional[Player] = None
    game: Optional[Game] = None
    color: Optional[GameColor] = None
    domain_null_exception = ArenaStackContextNullException()
    model_type = ArenaContext
