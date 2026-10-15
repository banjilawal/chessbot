# src/domain/extract/struct/binder/player/extract.py

"""
Module: domain.extract.struct.binder.player.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PlayerBinder, PlayerBinderBlueprint, BinderPrimeExtract
from transit import PlayerBinderCarrier


class PlayerBinderPrimeExtract(BinderPrimeExtract[PlayerBinder]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for PlayerBinderValidator.

    Attributes:
        carrier: PlayerBinderCarrier
        blueprint: Optional[PlayerBinderBlueprint]

    Provides:

    Super Class:
        BinderPrimeExtract
    """

    def __init__(
            self,
            reference: PlayerBinderCarrier,
            blueprint: Optional[PlayerBinderBlueprint] | None = None,
    ):
        """
        Args:
            reference: PlayerBinderCarrier
            blueprint: Optional[PlayerBinderBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> PlayerBinderCarrier:
        return cast(PlayerBinderCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PlayerBinderBlueprint]:
        return cast(PlayerBinderBlueprint, super().blueprint)