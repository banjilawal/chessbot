# src/blueprint/model/token/blueprint.py

"""
Module: blueprint.model.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from blueprint import Blueprint
from err import TokenNullException
from model.catalog import Formation
from model import HomeSquare, Rank, Team, Token


@dataclass
class TokenBlueprint(Blueprint[Token]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Token object.

    Attributes:
        id: Optional[int]
        team: Team
        rank: Rank
        formation: Formation
        home_square: OpeningSquare
        null_exception: TokenNullException
        model_type: Token
        
    Provides:

     Super Class:
        Blueprint
     """
    team: Team
    formation: Formation
    id: Optional[int] | None = None
    rank: Optional[Rank] | None = None
    home_square: HomeSquare | None = None
    null_exception: TokenNullException = TokenNullException()
    model_type: Token = Token
