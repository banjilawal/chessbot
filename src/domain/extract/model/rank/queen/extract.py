# src/domain/extract/model/rank/queen/extract.py

"""
Module: domain.extract.model.rank.queen.extract
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
            reference: QueenCarrier,
            safe_blueprint: Optional[QueenBlueprint] | None = None,
    ):
        """
        Args:
            reference: QueenCarrier
            safe_blueprint: Optional[QueenBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> QueenCarrier:
        return cast(QueenCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[QueenBlueprint]:
        return cast(QueenBlueprint, super().blueprint)