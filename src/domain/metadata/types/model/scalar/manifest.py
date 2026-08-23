# src/domain/metadata/types/model/scalar/manifest.py

"""
Module: domain.metadata.types.model.scalar.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Scalar, ScalarBlueprint, ScalarCarrier


@dataclass
class ScalarAssociationManifest(ModelAssociationManifest[Scalar]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Scalar uses in the domain.

    Attributes:
        model: Type[Scalar] = Scalar
        carrier: Type[ScalarCarrier] = ScalarCarrier
        blueprint: Type[ScalarBlueprint] = ScalarBlueprint
        search_context: Type[ScalarSearchContext] = ScalarSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Scalar] = Scalar
    carrier: Type[ScalarCarrier] = ScalarCarrier
    blueprint: Type[ScalarBlueprint] = ScalarBlueprint