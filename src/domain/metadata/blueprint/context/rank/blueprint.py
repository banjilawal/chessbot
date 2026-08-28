# src/domain/metadata/blueprint/context/rank/blueprint.py

"""
Module: domain.metadata.blueprint.context.rank.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import RankSearchContextNullException
from domain.model import RankContext, Blueprint, Game, Player


@dataclass
class RankContextBlueprint(Blueprint[RankContext]):
    """
     Role:
        1.  Metadata

    Responsibilities:
        1.  Provides values for hydrating a RankContext instance.

    Attributes:
        id: Optional[int]
        name: Optional[str]
        player: Optional[Player]
        game: Optional[Game]
        domain_null_exception = RankContextNullException
        model_type = RankContext

    Provides:

    Super Class:
        ContextBlueprint
    """
    id: Optional[int] = None,
    name: Optional[str] = None,
    player: Optional[Player] = None,
    game: Optional[Game] = None,
    domain_null_exception = RankSearchContextNullException()
    model_type = RankContext
    
