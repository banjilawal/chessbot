# src/domain/metadata/types/model/coord/manifest.py

"""
Module: domain.metadata.types.model.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Coord, CoordBlueprint, CoordCarrier, CoordSearchContext


@dataclass
class CoordAssociationManifest(ModelAssociationManifest[Coord]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Coord uses in the domain.

    Attributes:
        model: Type[Coord] = Coord
        carrier: Type[CoordCarrier] = CoordCarrier
        blueprint: Type[CoordBlueprint] = CoordBlueprint
        search_context: Type[CoordSearchContext] = CoordSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Coord] = Coord
    carrier: Type[CoordCarrier] = CoordCarrier
    blueprint: Type[CoordBlueprint] = CoordBlueprint
    search_context: Type[CoordSearchContext] = CoordSearchContext