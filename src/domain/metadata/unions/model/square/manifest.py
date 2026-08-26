# src/domain/metadata/unions/model/square/manifest.py

"""
Module: domain.metadata.unions.model.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Square, SquareBlueprint, SquareCarrier, SquareSearchSearchContext


@dataclass
class SquareTypeUnions(ModelTypeUnions[Square]):
    """
    Role:
        -  Metadata

    Responsibilities:
        1. Catalog of data unions a Square uses in the domain.

    Attributes:
        model: Type[Square] = Square
        carrier: Type[SquareCarrier] = SquareCarrier
        blueprint: Type[SquareBlueprint] = SquareBlueprint
        search_context: Type[SquareSearchContext] = SquareSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Square] = Square
    carrier: Type[SquareCarrier] = SquareCarrier
    blueprint: Type[SquareBlueprint] = SquareBlueprint
    search_context: Type[SquareSearchSearchContext] = SquareSearchSearchContext