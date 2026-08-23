# src/domain/metadata/types/model/game/manifest.py

"""
Module: domain.metadata.types.model.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelAssociationManifest, Game, GameBlueprint, GameCarrier, GameSearchContext


@dataclass
class GameAssociationManifest(ModelAssociationManifest[Game]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of data types a Game uses in the domain.

    Attributes:
        model: Type[Game] = Game
        carrier: Type[GameCarrier] = GameCarrier
        blueprint: Type[GameBlueprint] = GameBlueprint
        search_context: Type[GameSearchContext] = GameSearchContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Game] = Game
    carrier: Type[GameCarrier] = GameCarrier
    blueprint: Type[GameBlueprint] = GameBlueprint
    search_context: Type[GameSearchContext] = GameSearchContext