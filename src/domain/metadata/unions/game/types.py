# src/domain/metadata/unions/game/manifest.py

"""
Module: domain.metadata.unions.game.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from domain import Game, GameBlueprint, TypeUnion
from transit import GameCarrier


@dataclass
class GameTypeUnion(TypeUnion[Game]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions an Game uses in the domain.

    Attributes:
        model: Type[Game] = Game
        carrier: Type[GameCarrier] = GameCarrier
        blueprint: Type[GameBlueprint] = GameBlueprint
    
    Provides:

    Super Class:
        TypeUnion
    """
    model: Type[Game] = Game
    carrier: Type[GameCarrier] = GameCarrier
    blueprint: Type[GameBlueprint] = GameBlueprint