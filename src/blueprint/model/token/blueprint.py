# src/blueprint/model/token/blueprint.py

"""
Module: blueprint.model.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Type

from blueprint import Blueprint
from model import HomeSquare, Rank, Team, Token
from schema import Formation


@dataclass
class TokenBlueprint(Blueprint[Token]):
    """
    Role:
        -   Container
        -   DTO
        
    Responsibilities:
        1.  Provides values for instantiating a Token object.
        2.  DTO
        
    Attributes:
        id: Optional[int]
        team: Team
        rank: Rank
        formation: Formation
        home_square: OpeningSquare
        
    Provides:

     Super Class:
        Blueprint
     """
    """
    Args:
        team: Team
        formation: Formation
        id: Optional[int]
        rank: Optional[Rank]
        home_square: HomeSquare
        owner: Token
        owner_name: str
    """
    team: Team
    formation: Formation
    id: Optional[int] | None = None
    rank: Optional[Rank] | None = None
    home_square: HomeSquare | None = None
    owner: Token = Type[Token]
    owner_name: str = type(owner).__name__
