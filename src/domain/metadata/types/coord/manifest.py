# src/domain/metadata/types/coord/manifest.py

"""
Module: domain.metadata.types.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import CoordBlueprint
from domain.model import Coord
from domain.transit import CoordCarrier


@dataclass
class CoordTypes(TypesManifest[Coord]):
    model: Type[Coord] = Coord
    carrier: Type[CoordCarrier] = CoordCarrier
    blueprint: Type[CoordBlueprint] = CoordBlueprint