# src/domain/metadata/unions/model/searchable/state/game/manifest.py

"""
Module: domain.metadata.unions.model.searchable.state.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from domain import ModelTypeUnions, Game, GameBlueprint, GameCarrier, GameSearchContext


@dataclass
class GameTypeUnions(ModelTypeUnions[Game]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Game uses in the domain.

    Attributes:
        model: Type[Game] = Game
        carrier: Type[GameCarrier] = GameCarrier
        blueprint: Type[GameBlueprint] = GameBlueprint
        search_context: Type[GameContext] = GameContext
    
    Provides:

    Super Class:
        ModelManifest
    """
    model: Type[Game] = Game
    carrier: Type[GameCarrier] = GameCarrier
    blueprint: Type[GameBlueprint] = GameBlueprint
    search_context: Type[GameSearchContext] = GameSearchContext