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

from domain import Knight, KnightBlueprint, RankTypeUnion
from transit import KnightCarrier


@dataclass
class KnightTypeUnion(RankTypeUnion[Knight]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Knight uses in the domain.

    Attributes:
        model: Type[Knight] = Knight
        carrier: Type[KnightCarrier] = KnightCarrier
        blueprint: Type[KnightBlueprint] = KnightBlueprint
    
    Provides:

    Super Class:
        RankTypeUnion
    """
    model: Type[Knight] = Knight
    carrier: Type[KnightCarrier] = KnightCarrier
    blueprint: Type[KnightBlueprint] = KnightBlueprint