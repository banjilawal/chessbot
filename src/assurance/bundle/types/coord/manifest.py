# src/assurance/manifest/types/coord/manifest.py

"""
Module: assurance.manifest.types.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import CoordBlueprint
from model import Coord
from transit import CoordCarrier


@dataclass(frozen=True)
class CoordTypes(TypesManifest[Coord]):
    model: Type[Coord] = Coord
    carrier: Type[CoordCarrier] = CoordCarrier
    blueprint: Type[CoordBlueprint] = CoordBlueprint