# src/domain/metadata/nulls/model/game/roster.py

"""
Module: domain.metadata.nulls.model.game.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Game
from err import (
    GameBlueprintNullException, GameCarrierNullException, GameStackContextNullException, GameNullException
)


@dataclass
class GameNullExceptionRoster(ModelNullExceptionRoster[Game]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Game.

    Attributes:
        model: GameNullException
        carrier: GameCarrierNullException
        blueprint: GameBlueprintNullException
        search_context: GameContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: GameNullException = GameNullException()
    carrier: GameCarrierNullException = GameCarrierNullException()
    blueprint: GameBlueprintNullException = GameBlueprintNullException()
    search_context: GameStackContextNullException = GameStackContextNullException()