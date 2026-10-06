# src/domain/extract/model/rank/rook/extract.py

"""
Module: domain.extract.model.rank.rook.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Rook, RookBlueprint, RankPrimeExtract
from transit import RookCarrier


class RookPrimeExtract(RankPrimeExtract[Rook]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for RookValidator.

    Attributes:
        carrier: RookCarrier
        blueprint: Optional[RookBlueprint]

    Provides:

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            reference: RookCarrier,
            blueprint: Optional[RookBlueprint] | None = None,
    ):
        """
        Args:
            reference: RookCarrier
            blueprint: Optional[RookBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> RookCarrier:
        return cast(RookCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[RookBlueprint]:
        return cast(RookBlueprint, super().blueprint)