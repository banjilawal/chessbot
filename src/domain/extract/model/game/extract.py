# src/domain/extract/model/game/extract.py

"""
Module: domain.extract.model.game.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Game, GameBlueprint
from transit import GameCarrier


class GamePrimeExtract(ModelPrimeExtract[Game]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for GameValidator.

    Attributes:
        carrier: GameCarrier
        blueprint: Optional[GameBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: GameCarrier,
            blueprint: Optional[GameBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Game]
            blueprint: Optional[Blueprint[Game]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> GameCarrier:
        return cast(GameCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[GameBlueprint]:
        return cast(GameBlueprint, super().blueprint)