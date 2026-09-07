# src/domain/metadata/unions/token/king/manifest.py

"""
Module: domain.metadata.unions.token.king.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import KingToken, TokenTypeUnion
from transit import KingCarrier


@dataclass
class KingTokenTypeUnion(TokenTypeUnion[KingToken]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a King uses in the domain.

    Attributes:
        model: Type[KingToken] = KingToken
        carrier: Type[KingTokenCarrier] = KingCarrier
        blueprint: Type[KingTokenBlueprint] = KingBlueprint
    
    Provides:

    Super Class:
        TokenTypeUnion
    """
    model: Type[KingToken] = KingToken
    carrier: Type[KingTokenCarrier] = KingTokenCarrier
    blueprint: Type[KingTokenBlueprint] = KingTokenBlueprint