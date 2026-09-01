# src/domain/metadata/unions/player/manifest.py

"""
Module: domain.metadata.unions.player.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Player, PlayerBlueprint
from transit import PlayerCarrier


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
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Player] = Player
    carrier: Type[PlayerCarrier] = PlayerCarrier
    blueprint: Type[PlayerBlueprint] = PlayerBlueprint