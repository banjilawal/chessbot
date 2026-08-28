# src/domain/metadata/blueprint/validation/rank/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import RankNullException
from domain.model import Rank, Blueprint, Game, Player


@dataclass
class RankQueryValidationBlueprint(QueryValidationBlueprint[Rank]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a RankValidation instance.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        player: Optional[Player]
        game: Optional[Game]
        domain_null_exception = RankNullException
        model_type = RankValidation

    Provides:

    Super Class:
        QueryValidationBlueprint
    """
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    domain_null_exception = RankNullException()
    model_type = RankValidation
    
