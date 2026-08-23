# src/domain/metadata/unions/model/vector/manifest.py

"""
Module: domain.metadata.unions.model.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Vector, VectorBlueprint, VectorCarrier


@dataclass
class VectorTypeUnions(ModelTypeUnions[Vector]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data unions a Vector uses in the domain.

    Attributes:
        model: Type[Vector] = Vector
        carrier: Type[VectorCarrier] = VectorCarrier
        blueprint: Type[VectorBlueprint] = VectorBlueprint
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Vector] = Vector
    carrier: Type[VectorCarrier] = VectorCarrier
    blueprint: Type[VectorBlueprint] = VectorBlueprint