# src/domain/extract/model/rank/king/extract.py

"""
Module: domain.extract.model.rank.king.extract
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

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            reference: KingCarrier,
            safe_blueprint: Optional[KingBlueprint] | None = None,
    ):
        """
        Args:
            reference: KingCarrier
            safe_blueprint: Optional[KingBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> KingCarrier:
        return cast(KingCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[KingBlueprint]:
        return cast(KingBlueprint, super().blueprint)