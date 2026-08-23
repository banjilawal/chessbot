# src/domain/metadata/types/model/vector/manifest.py

"""
Module: domain.metadata.types.model.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Vector, VectorBlueprint, VectorCarrier


@dataclass
class VectorAssociationManifest(ModelAssociationManifest[Vector]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Vector uses in the domain.

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