# src/domain/extract/context/game/extract.py

"""
Module: domain.extract.context.game.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameContextBlueprint, ContextPrimeExtract
from transit import GameContextCarrier


class GameContextPrimeExtract(ContextPrimeExtract[GameContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for GameValidator.

    Attributes:
        contextCarrier: GameContextCarrier
        blueprint: Optional[GameContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: GameContextCarrier,
            blueprint: Optional[GameContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: GameContextCarrier
            blueprint: Optional[ContextBlueprint[Game]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> GameContextCarrier:
        return cast(GameContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[GameContextBlueprint]:
        return cast(GameContextBlueprint, super().blueprint)