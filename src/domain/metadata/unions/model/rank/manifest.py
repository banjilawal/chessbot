# src/domain/metadata/unions/model/rank/manifest.py

"""
Module: domain.metadata.unions.model.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Rank, RankBlueprint, RankCarrier, RankSearchContext


@dataclass
class RankTypeUnions(ModelTypeUnions[Rank]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data unions a Rank uses in the domain.

    Attributes:
        model: Type[Rank] = Rank
        carrier: Type[RankCarrier] = RankCarrier
        blueprint: Type[RankBlueprint] = RankBlueprint
        search_context: Type[RankSearchContext] = RankSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Rank] = Rank
    carrier: Type[RankCarrier] = RankCarrier
    blueprint: Type[RankBlueprint] = RankBlueprint
    search_context: Type[RankSearchContext] = RankSearchContext