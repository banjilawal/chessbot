# src/domain/metadata/unions/model/searchable/state/player/manifest.py

"""
Module: domain.metadata.unions.model.searchable.state.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Player, PlayerBlueprint, PlayerCarrier, PlayerSearchContext


@dataclass
class PlayerTypeUnions(ModelTypeUnions[Player]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Player uses in the domain.

    Attributes:
        model: Type[Player] = Player
        carrier: Type[PlayerCarrier] = PlayerCarrier
        blueprint: Type[PlayerBlueprint] = PlayerBlueprint
        search_context: Type[PlayerContext] = PlayerContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Player] = Player
    carrier: Type[PlayerCarrier] = PlayerCarrier
    blueprint: Type[PlayerBlueprint] = PlayerBlueprint
    search_context: Type[PlayerSearchContext] = PlayerSearchContext