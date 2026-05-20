# src/blueprint/context/arena/blueprint.py

"""
Module: blueprint.context.arena.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from err import ArenaContextNullException
from model import ArenaContext, Blueprint, Game, Player
from setting import GameColor


@dataclass
class ArenaContextBlueprint(Blueprint[ArenaContext]):
    id: Optional[int] = None
    name: Optional[str] = None
    player: Optional[Player] = None
    game: Optional[Game] = None
    color: Optional[GameColor] = None
    null_exception = ArenaContextNullException()
    model_type = ArenaContext
