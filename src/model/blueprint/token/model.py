# src/model/blueprint/token/model.py

"""
Module: model.blueprint.token.model
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
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Token object.

    Attributes:
        id: int
        team: Team
        rank: Rank
        formation: Formation
        opening_square: OpeningSquare

    Provides:

     Super Class:
        Blueprint
     """
    team: Team
    formation: Formation
    id: int | None = None
    rank: Rank | None = None
    opening_square: OpeningSquare | None = None
