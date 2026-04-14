# src/model/blueprint/context/team/blueprint.py

"""
Module: model.blueprint.context.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import Board, Blueprint, Player, Schema, TeamContext, TeamState


@dataclass
class TeamContextBlueprint(Blueprint[TeamContext]):
    id: Optional[int] = None | None
    board: Optional[Board] = None | None
    player: Optional[Player] = None | None
    state: Optional[TeamState] = None | None
    schema: Optional[Schema] = None | None
