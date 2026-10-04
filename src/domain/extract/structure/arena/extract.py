# src/domain/extract/struct/arena/extract.py

"""
Module: domain.extract.struct.arena.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import StructPrimeExtract
from domain import Arena, ArenaBlueprint
from transit import ArenaCarrier


class ArenaPrimeExtract(StructPrimeExtract[Arena]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ArenaValidator.

    Attributes:
        carrier: ArenaCarrier
        blueprint: Optional[ArenaBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: ArenaCarrier,
            blueprint: Optional[ArenaBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Arena]
            blueprint: Optional[Blueprint[Arena]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> ArenaCarrier:
        return cast(ArenaCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[ArenaBlueprint]:
        return cast(ArenaBlueprint, super().blueprint)