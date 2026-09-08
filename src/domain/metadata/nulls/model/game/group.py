# src/domain/metadata/nulls/model/game/group.py

"""
Module: domain.metadata.nulls.model.game.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import (
    GameBlueprintNullException, GameCarrierNullException, GameNullException
)


class GameNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Game's integrity cycle.

    Attributes:
        model: GameNullException
        carrier: GameCarrierNullException
        blueprint: GameBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[GameNullException] | None = None,
            carrier: Optional[GameCarrierNullException] | None = None,
            blueprint: Optional[GameBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[GameNullException]
            carrier: Optional[GameCarrierNullException]
            blueprint: Optional[GameBlueprintNullException]
        """
        super().__init__(
            model = model or GameNullException(),
            carrier = carrier or GameCarrierNullException(),
            blueprint = blueprint or GameBlueprintNullException(),
        )
        
    @property
    def model(self) -> GameNullException:
        return cast(GameNullException, super().model)
    
    @property
    def carrier(self) -> GameCarrierNullException:
        return cast(GameCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> GameBlueprintNullException:
        return cast(GameBlueprintNullException, super().blueprint)