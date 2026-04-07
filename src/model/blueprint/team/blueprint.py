# src/model/blueprint/team/blueprint.py

"""
Module: model.blueprint.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from catalog import Schema
from model import Blueprint, Board, Player, Team


@dataclass
class TeamBlueprint(Blueprint[Team]):
    owner: Player
    board: Board
    schema: Schema
