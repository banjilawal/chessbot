# src/domain/metadata/null/context/player/null.py

"""
Module: domain.metadata.null.context.player.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullWarningSet, Player
from err import (
    PlayerContextBlueprintNullException, PlayerContextCarrierNullException, PlayerContextNullException
)


class PlayerContextNullWarningSet(ContextNullWarningSet[PlayerContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Player's integrity cycle.

    Attributes:
        model: PlayerContextNullException
        carrier: PlayerContextCarrierNullException
        blueprint: PlayerContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[PlayerContextNullException] | None = None,
            carrier: Optional[PlayerContextCarrierNullException] | None = None,
            blueprint: Optional[PlayerContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PlayerContextNullException]
            carrier: Optional[PlayerContextCarrierNullException]
            blueprint: Optional[PlayerContextBlueprintNullException]
        """
        super().__init__(
            model=model or PlayerContextNullException(),
            carrier=carrier or PlayerContextCarrierNullException(),
            blueprint=blueprint or PlayerContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> PlayerContextNullException:
        return cast(PlayerContextNullException, super().model)
    
    @property
    def carrier(self) -> PlayerContextCarrierNullException:
        return cast(PlayerContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PlayerContextBlueprintNullException:
        return cast(PlayerContextBlueprintNullException, super().blueprint)