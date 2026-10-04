# src/domain/extract/struct/rank/pawn/extract.py

"""
Module: domain.extract.struct.rank.pawn.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Pawn, PawnBlueprint, RankPrimeExtract
from transit import PawnCarrier


class PawnPrimeExtract(RankPrimeExtract[Pawn]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for PawnValidator.

    Attributes:
        carrier: PawnCarrier
        blueprint: Optional[PawnBlueprint]

    Provides:

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            carrier: PawnCarrier,
            blueprint: Optional[PawnBlueprint] | None = None,
    ):
        """
        Args:
            carrier: PawnCarrier
            blueprint: Optional[PawnBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> PawnCarrier:
        return cast(PawnCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[PawnBlueprint]:
        return cast(PawnBlueprint, super().blueprint)