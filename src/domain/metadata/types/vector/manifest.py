# src/domain/metadata/types/vector/manifest.py

"""
Module: domain.metadata.types.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import VectorBlueprint
from domain.model import Vector
from domain.transit import VectorCarrier


@dataclass
class VectorTypes(TypesManifest[Vector]):
    model: Type[Vector] = Vector
    carrier: Type[VectorCarrier] = VectorCarrier
    blueprint: Type[VectorBlueprint] = VectorBlueprint