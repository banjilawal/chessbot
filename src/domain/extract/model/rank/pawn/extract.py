# src/domain/extract/model/rank/pawn/extract.py

"""
Module: domain.extract.model.rank.pawn.extract
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
            reference: PawnCarrier,
            safe_blueprint: Optional[PawnBlueprint] | None = None,
    ):
        """
        Args:
            reference: PawnCarrier
            safe_blueprint: Optional[PawnBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> PawnCarrier:
        return cast(PawnCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[PawnBlueprint]:
        return cast(PawnBlueprint, super().blueprint)