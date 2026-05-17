# src/model/blueprint/context/player/blueprint.py

"""
Module: model.blueprint.context.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import PlayerContextNullException
from model import PlayerContext, Blueprint, Game, Team


@dataclass
class PlayerContextBlueprint(Blueprint[PlayerContext]):
    id: Optional[id] = None
    name: Optional[str] = None
    team: Optional[Team] = None
    game: Optional[Game] = None
    class_name: Optional[str] = None
    null_exception = PlayerContextNullException()
    model_type = PlayerContext
