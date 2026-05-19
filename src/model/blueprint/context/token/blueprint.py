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

from err import TokenContextNullException
from model import Coord, OpeningSquare, Rank, Team, TokenContext, Blueprint
from setting import GameColor


@dataclass
class TokenContextBlueprint(Blueprint[TokenContext]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a TokenContext instance.

    Attributes:
        rank: Optional[Rank]
        team: Optional[Team]
        ransom: Optional[int]
        color: Optional[GameColor]
        designation: Optional[str]
        current_position: Optional[Coord]
        opening_square: Optional[OpeningSquare]
        null_exception = TokenContextNullException()
        model_type = TokenContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] | None = None
    rank: Optional[Rank] | None = None
    team: Optional[Team] | None = None
    ransom: Optional[int] | None = None
    color: Optional[GameColor] | None = None
    designation: Optional[str] | None = None
    current_position: Optional[Coord] | None = None
    opening_square: Optional[OpeningSquare] | None = None
    null_exception = TokenContextNullException()
    model_type = TokenContext

