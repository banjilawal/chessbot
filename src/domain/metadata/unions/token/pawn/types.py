# src/domain/metadata/unions/token/pawn/manifest.py

"""
Module: domain.metadata.unions.token.pawn.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Pawn, PawnBlueprint, TokenTypeUnion
from transit import PawnCarrier


@dataclass
class PawnTypeUnion(TokenTypeUnion[Pawn]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Pawn uses in the domain.

    Attributes:
        model: Type[Pawn] = Pawn
        carrier: Type[PawnCarrier] = PawnCarrier
        blueprint: Type[PawnBlueprint] = PawnBlueprint
    
    Provides:

    Super Class:
        TokenTypeUnion
    """
    model: Type[Pawn] = Pawn
    carrier: Type[PawnCarrier] = PawnCarrier
    blueprint: Type[PawnBlueprint] = PawnBlueprint