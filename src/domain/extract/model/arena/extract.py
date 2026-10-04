# src/domain/extract/model/arena/extract.py

"""
Module: domain.extract.model.arena.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaBlueprint, ModelPrimeExtract
from transit import ArenaCarrier


class ArenaPrimeExtract(ModelPrimeExtract[Arena]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ArenaValidator.

    Attributes:
        carrier: ArenaCarrier
        blueprint: Optional[ArenaBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: ArenaCarrier,
            blueprint: Optional[ArenaBlueprint] | None = None,
    ):
        """
        Args:
            carrier: ArenaCarrier
            blueprint: Optional[Blueprint[Arena]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> ArenaCarrier:
        return cast(ArenaCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[ArenaBlueprint]:
        return cast(ArenaBlueprint, super().blueprint)