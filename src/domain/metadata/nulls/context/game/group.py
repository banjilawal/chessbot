# src/domain/metadata/nulls/context/game/group.py

"""
Module: domain.metadata.nulls.context.game.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, ContextNullGroup
from err import (
    GameContextBlueprintNullException, GameContextCarrierNullException, GameContextNullException
)


class GameContextNullGroup(ContextNullGroup[GameContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Game's integrity cycle.

    Attributes:
        context: GameContextNullException
        carrier: GameContextCarrierNullException
        blueprint: GameContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[GameContextNullException] | None = None,
            carrier: Optional[GameContextCarrierNullException] | None = None,
            blueprint: Optional[GameContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[GameContextNullException]
            carrier: Optional[GameContextCarrierNullException]
            blueprint: Optional[GameContextBlueprintNullException]
        """
        super().__init__(
            context = context or GameContextNullException(),
            carrier = carrier or GameContextCarrierNullException(),
            blueprint = blueprint or GameContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> GameContextNullException:
        return cast(GameContextNullException, super().context)
    
    @property
    def carrier(self) -> GameContextCarrierNullException:
        return cast(GameContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> GameContextBlueprintNullException:
        return cast(GameContextBlueprintNullException, super().blueprint)