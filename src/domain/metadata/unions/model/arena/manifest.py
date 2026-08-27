# src/domain/metadata/unions/model/arena/manifest.py

"""
Module: domain.metadata.unions.model.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Arena, ArenaBlueprint, ArenaCarrier, ArenaSearchSearchContext


@dataclass
class ArenaTypeUnions(ModelTypeUnions[Arena]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Arena uses in the domain.

    Attributes:
        model: Type[Arena] = Arena
        carrier: Type[ArenaCarrier] = ArenaCarrier
        blueprint: Type[ArenaBlueprint] = ArenaBlueprint
        search_context: Type[ArenaSearchContext] = ArenaSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Arena] = Arena
    carrier: Type[ArenaCarrier] = ArenaCarrier
    blueprint: Type[ArenaBlueprint] = ArenaBlueprint
    search_context: Type[ArenaSearchSearchContext] = ArenaSearchSearchContext