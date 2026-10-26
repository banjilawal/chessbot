# src/domain/metadata/null/context/game/null.py

"""
Module: domain.metadata.null.context.game.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, ContextNullWarningSet
from err import (
    GameContextBlueprintNullException, GameContextCarrierNullException, GameContextNullException
)


class GameContextNullWarningSet(ContextNullWarningSet[GameContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Game's integrity cycle.

    Attributes:
        model: GameContextNullException
        carrier: GameContextCarrierNullException
        blueprint: GameContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[GameContextNullException] | None = None,
            carrier: Optional[GameContextCarrierNullException] | None = None,
            blueprint: Optional[GameContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[GameContextNullException]
            carrier: Optional[GameContextCarrierNullException]
            blueprint: Optional[GameContextBlueprintNullException]
        """
        super().__init__(
            model=model or GameContextNullException(),
            carrier=carrier or GameContextCarrierNullException(),
            blueprint=blueprint or GameContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> GameContextNullException:
        return cast(GameContextNullException, super().model)
    
    @property
    def carrier(self) -> GameContextCarrierNullException:
        return cast(GameContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> GameContextBlueprintNullException:
        return cast(GameContextBlueprintNullException, super().blueprint)