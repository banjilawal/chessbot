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

from domain import Queen, QueenBlueprint, RankTypeUnion
from transit import QueenCarrier


@dataclass
class QueenTypeUnion(RankTypeUnion[Queen]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Queen uses in the domain.

    Attributes:
        model: Type[Queen] = Queen
        carrier: Type[QueenCarrier] = QueenCarrier
        blueprint: Type[QueenBlueprint] = QueenBlueprint
    
    Provides:

    Super Class:
        RankTypeUnion
    """
    model: Type[Queen] = Queen
    carrier: Type[QueenCarrier] = QueenCarrier
    blueprint: Type[QueenBlueprint] = QueenBlueprint