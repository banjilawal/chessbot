# src/domain/metadata/unions/square/manifest.py

"""
Module: domain.metadata.unions.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Square, SquareBlueprint, TypeUnion
from transit import SquareCarrier


@dataclass
class SquareTypeUnion(TypeUnion[Square]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Square uses in the domain.

    Attributes:
        model: Type[Square] = Square
        carrier: Type[SquareCarrier] = SquareCarrier
        blueprint: Type[SquareBlueprint] = SquareBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Square] = Square
    carrier: Type[SquareCarrier] = SquareCarrier
    blueprint: Type[SquareBlueprint] = SquareBlueprint