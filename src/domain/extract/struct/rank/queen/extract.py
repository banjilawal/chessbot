# src/domain/extract/struct/rank/queen/extract.py

"""
Module: domain.extract.struct.rank.queen.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Queen, QueenBlueprint, RankPrimeExtract
from transit import QueenCarrier


class QueenPrimeExtract(RankPrimeExtract[Queen]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for QueenValidator.

    Attributes:
        carrier: QueenCarrier
        blueprint: Optional[QueenBlueprint]

    Provides:

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            carrier: QueenCarrier,
            blueprint: Optional[QueenBlueprint] | None = None,
    ):
        """
        Args:
            carrier: QueenCarrier
            blueprint: Optional[QueenBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> QueenCarrier:
        return cast(QueenCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[QueenBlueprint]:
        return cast(QueenBlueprint, super().blueprint)