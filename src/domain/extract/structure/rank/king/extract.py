# src/domain/extract/struct/rank/king/extract.py

"""
Module: domain.extract.struct.rank.king.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import King, KingBlueprint, RankPrimeExtract
from transit import KingCarrier


class KingPrimeExtract(RankPrimeExtract[King]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for KingValidator.

    Attributes:
        carrier: KingCarrier
        blueprint: Optional[KingBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            carrier: KingCarrier,
            blueprint: Optional[KingBlueprint] | None = None,
    ):
        """
        Args:
            carrier: KingCarrier
            blueprint: Optional[KingBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> KingCarrier:
        return cast(KingCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[KingBlueprint]:
        return cast(KingBlueprint, super().blueprint)