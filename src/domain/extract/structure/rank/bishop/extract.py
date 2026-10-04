# src/domain/extract/struct/rank/bishop/extract.py

"""
Module: domain.extract.struct.rank.bishop.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, BishopBlueprint, RankPrimeExtract
from transit import BishopCarrier


class BishopPrimeExtract(RankPrimeExtract[Bishop]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for BishopValidator.

    Attributes:
        carrier: BishopCarrier
        blueprint: Optional[BishopBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            carrier: BishopCarrier,
            blueprint: Optional[BishopBlueprint] | None = None,
    ):
        """
        Args:
            carrier: BishopCarrier
            blueprint: Optional[BishopBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> BishopCarrier:
        return cast(BishopCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[BishopBlueprint]:
        return cast(BishopBlueprint, super().blueprint)