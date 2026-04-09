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

from model import Board, TeamContext, Blueprint, Game, Player


@dataclass
class TeamContextBlueprint(Blueprint[TeamContext]):
    board: Optional[Board] = None
    coord: Optional[Coord] = None
    occupant: Optional[Token] = None
    state: Optional[SquareState] = None
    formation: Optional[Formation] = None
