# src/domain/metadata/unions/coord/manifest.py

"""
Module: domain.metadata.unions.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Coord, CoordBlueprint, TypeUnion
from transit import CoordCarrier


@dataclass
class CoordTypeUnion(TypeUnion[Coord]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Coord uses in the domain.

    Attributes:
        model: Type[Coord] = Coord
        carrier: Type[CoordCarrier] = CoordCarrier
        blueprint: Type[CoordBlueprint] = CoordBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Coord] = Coord
    carrier: Type[CoordCarrier] = CoordCarrier
    blueprint: Type[CoordBlueprint] = CoordBlueprint