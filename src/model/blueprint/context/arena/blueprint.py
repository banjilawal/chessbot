# src/model/blueprint/context/arena/blueprint.py

"""
Module: model.blueprint.context.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import ArenaContext, Blueprint, Game, Player


@dataclass
class ArenaContextBlueprint(Blueprint[ArenaContext]):
    id: Optional[int] = None
    name: Optional[str] = None
    player: Optional[Player] = None
    game: Optional[Game] = None
