# src/domain/extract/model/player/extract.py

"""
Module: domain.extract.model.player.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast


from domain import ModelPrimeExtract, Player, PlayerBlueprint
from transit import PlayerCarrier


class PlayerPrimeExtract(ModelPrimeExtract[Player]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for PlayerValidator.

    Attributes:
        carrier: PlayerCarrier
        blueprint: Optional[PlayerBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: PlayerCarrier,
            blueprint: Optional[PlayerBlueprint] | None = None,
    ):
        """
        Args:
            reference: EntityCarrier[Player]
            blueprint: Optional[Blueprint[Player]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PlayerCarrier:
        return cast(PlayerCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PlayerBlueprint]:
        return cast(PlayerBlueprint, super().blueprint)