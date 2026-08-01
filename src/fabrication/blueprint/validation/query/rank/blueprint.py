# src/blueprint/validation/rank/blueprint.py

"""
Module: blueprint.validation.query.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import RankNullException
from model import Rank, Blueprint, Game, Player


@dataclass
class RankQueryValidationBlueprint(QueryValidationBlueprint[Rank]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a RankValidation instance.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        player: Optional[Player]
        game: Optional[Game]
        null_exception = RankNullException
        model_type = RankValidation

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    null_exception = RankNullException()
    model_type = RankValidation
    
