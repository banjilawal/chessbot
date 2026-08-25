# src/domain/metadata/nulls/model/player/roster.py

"""
Module: domain.metadata.nulls.model.player.roster
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass

from domain import ModelNullExceptionRoster, Player
from err import (
    PlayerBlueprintNullException, PlayerCarrierNullException, PlayerStackContextNullException, PlayerNullException
)


@dataclass
class PlayerNullExceptionRoster(ModelNullExceptionRoster[Player]):
    """
    Role:
        -   Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Player.

    Attributes:
        model: PlayerNullException
        carrier: PlayerCarrierNullException
        blueprint: PlayerBlueprintNullException
        search_context: PlayerContextNullException

    Provides:

    Super Class:
        ModelNullExceptionRoster
    """
    model: PlayerNullException = PlayerNullException()
    carrier: PlayerCarrierNullException = PlayerCarrierNullException()
    blueprint: PlayerBlueprintNullException = PlayerBlueprintNullException()
    search_context: PlayerStackContextNullException = PlayerStackContextNullException()