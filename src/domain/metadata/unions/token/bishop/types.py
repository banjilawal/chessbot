# src/domain/metadata/unions/token/bishop/manifest.py

"""
Module: domain.metadata.unions.token.bishop.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Bishop, BishopBlueprint, TokenTypeUnion
from transit import BishopCarrier


@dataclass
class BishopTypeUnion(TokenTypeUnion[Bishop]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Bishop uses in the domain.

    Attributes:
        model: Type[Bishop] = Bishop
        carrier: Type[BishopCarrier] = BishopCarrier
        blueprint: Type[BishopBlueprint] = BishopBlueprint
    
    Provides:

    Super Class:
        TokenTypeUnion
    """
    model: Type[Bishop] = Bishop
    carrier: Type[BishopCarrier] = BishopCarrier
    blueprint: Type[BishopBlueprint] = BishopBlueprint