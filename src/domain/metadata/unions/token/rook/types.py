# src/domain/metadata/unions/token/rook/manifest.py

"""
Module: domain.metadata.unions.token.rook.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Rook, RookBlueprint, TokenTypeUnion
from transit import RookCarrier


@dataclass
class RookTypeUnion(TokenTypeUnion[Rook]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Rook uses in the domain.

    Attributes:
        model: Type[Rook] = Rook
        carrier: Type[RookCarrier] = RookCarrier
        blueprint: Type[RookBlueprint] = RookBlueprint
    
    Provides:

    Super Class:
        TokenTypeUnion
    """
    model: Type[Rook] = Rook
    carrier: Type[RookCarrier] = RookCarrier
    blueprint: Type[RookBlueprint] = RookBlueprint