# src/domain/metadata/unions/maneuver/manifest.py

"""
Module: domain.metadata.unions.maneuver.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Maneuver, ManeuverBlueprint, TypeUnion
from transit import ManeuverCarrier


@dataclass
class ManeuverTypeUnion(TypeUnion[Maneuver]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Maneuver uses in the domain.

    Attributes:
        model: Type[Maneuver] = Maneuver
        carrier: Type[ManeuverCarrier] = ManeuverCarrier
        blueprint: Type[ManeuverBlueprint] = ManeuverBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Maneuver] = Maneuver
    carrier: Type[ManeuverCarrier] = ManeuverCarrier
    blueprint: Type[ManeuverBlueprint] = ManeuverBlueprint