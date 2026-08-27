# src/domain/metadata/unions/model/searchable/cartesian/coord/manifest.py

"""
Module: domain.metadata.unions.model.searchable.cartesian.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Coord, CoordBlueprint, CoordCarrier, CoordSearchSearchContext


@dataclass
class CoordTypeUnions(ModelTypeUnions[Coord]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Coord uses in the domain.

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
    search_context: Type[CoordSearchSearchContext] = CoordSearchSearchContext