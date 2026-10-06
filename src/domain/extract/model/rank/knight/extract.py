# src/domain/extract/model/rank/knight/extract.py

"""
Module: domain.extract.model.rank.knight.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Knight, KnightBlueprint, RankPrimeExtract
from transit import KnightCarrier


class KnightPrimeExtract(RankPrimeExtract[Knight]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for KnightValidator.

    Attributes:
        carrier: KnightCarrier
        blueprint: Optional[KnightBlueprint]

    Provides:

    Super Class:
        RankPrimeExtract
    """

    def __init__(
            self,
            reference: KnightCarrier,
            blueprint: Optional[KnightBlueprint] | None = None,
    ):
        """
        Args:
            reference: KnightCarrier
            blueprint: Optional[KnightBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> KnightCarrier:
        return cast(KnightCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[KnightBlueprint]:
        return cast(KnightBlueprint, super().blueprint)