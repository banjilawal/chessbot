# src/domain/metadata/types/model/player/manifest.py

"""
Module: domain.metadata.types.model.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Player, PlayerBlueprint, PlayerCarrier, PlayerSearchContext


@dataclass
class PlayerAssociationManifest(ModelAssociationManifest[Player]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Player uses in the domain.

    Attributes:
        model: Type[Player] = Player
        carrier: Type[PlayerCarrier] = PlayerCarrier
        blueprint: Type[PlayerBlueprint] = PlayerBlueprint
        search_context: Type[PlayerSearchContext] = PlayerSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Player] = Player
    carrier: Type[PlayerCarrier] = PlayerCarrier
    blueprint: Type[PlayerBlueprint] = PlayerBlueprint
    search_context: Type[PlayerSearchContext] = PlayerSearchContext