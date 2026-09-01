# src/domain/metadata/unions/rank/manifest.py

"""
Module: domain.metadata.unions.rank.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import King, KingBlueprint, RankTypeUnion
from transit import KingCarrier


@dataclass
class KingTypeUnion(RankTypeUnion[King]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a King uses in the domain.

    Attributes:
        model: Type[King] = King
        carrier: Type[KingCarrier] = KingCarrier
        blueprint: Type[KingBlueprint] = KingBlueprint
    
    Provides:

    Super Class:
        RankTypeUnion
    """
    model: Type[King] = King
    carrier: Type[KingCarrier] = KingCarrier
    blueprint: Type[KingBlueprint] = KingBlueprint