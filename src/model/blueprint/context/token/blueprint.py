# src/model/blueprint/context/token/blueprint.py

"""
Module: model.blueprint.context.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import Coord, Rank, Team, TokenContext, Blueprint
from system import GameColor


@dataclass
class TokenContextBlueprint(Blueprint[TokenContext]):
    rank: Optional[Rank]
    team: Optional[Team]
    ransom: Optional[int]
    color: Optional[GameColor]
    designation: Optional[str]
    current_position: Optional[Coord]
    opening_square_name: Optional[str]
    null_exception: 

