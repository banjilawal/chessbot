# src/domain/metadata/types/model/arena/manifest.py

"""
Module: domain.metadata.types.model.arena.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Arena, ArenaBlueprint, ArenaCarrier, ArenaSearchContext


@dataclass
class ArenaAssociationManifest(ModelAssociationManifest[Arena]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Arena uses in the domain.

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
    search_context: Type[ArenaSearchContext] = ArenaSearchContext