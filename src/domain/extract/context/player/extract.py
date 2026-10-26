# src/domain/extract/context/player/extract.py

"""
Module: domain.extract.context.player.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast


from domain import ContextPrimeExtract, Player, PlayerContextBlueprint
from transit import PlayerContextCarrier


class PlayerContextPrimeExtract(ContextPrimeExtract[PlayerContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for PlayerValidator.

    Attributes:
        contextCarrier: PlayerContextCarrier
        blueprint: Optional[PlayerContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: PlayerContextCarrier,
            blueprint: Optional[PlayerContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: ContextCarrier[Player]
            blueprint: Optional[ContextBlueprint[Player]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PlayerContextCarrier:
        return cast(PlayerContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PlayerContextBlueprint]:
        return cast(PlayerContextBlueprint, super().blueprint)