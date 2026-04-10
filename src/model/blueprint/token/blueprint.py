# src/model/blueprint/token/blueprint.py

"""
Module: model.blueprint.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model.catalog import Formation
from model import Blueprint, OpeningSquare, Rank, Team, Token


@dataclass
class TokenBlueprint(Blueprint[Token]):
    team: Team
    formation: Formation
    rank: Rank | None = None
    id: int | None = None
    opening_square: OpeningSquare | None = None
