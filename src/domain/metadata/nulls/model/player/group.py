# src/domain/metadata/nulls/model/player/group.py

"""
Module: domain.metadata.nulls.model.player.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import NullExceptionGroup, Player
from err import (
    PlayerBlueprintNullException, PlayerCarrierNullException, PlayerNullException
)

T = TypeVar("T", bound="Player")

class PlayerNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Player's integrity cycle.

    Attributes:
        model: PlayerNullException
        carrier: PlayerCarrierNullException
        blueprint: PlayerBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[PlayerNullException] | None = None,
            carrier: Optional[PlayerCarrierNullException] | None = None,
            blueprint: Optional[PlayerBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PlayerNullException]
            carrier: Optional[PlayerCarrierNullException]
            blueprint: Optional[PlayerBlueprintNullException]
        """
        super().__init__(
            model = model or PlayerNullException(),
            carrier = carrier or PlayerCarrierNullException(),
            blueprint = blueprint or PlayerBlueprintNullException(),
        )
        
    @property
    def model(self) -> PlayerNullException:
        return cast(PlayerNullException, super().model)
    
    @property
    def carrier(self) -> PlayerCarrierNullException:
        return cast(PlayerCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PlayerBlueprintNullException:
        return cast(PlayerBlueprintNullException, super().blueprint)