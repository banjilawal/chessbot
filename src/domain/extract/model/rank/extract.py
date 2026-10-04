# src/domain/extract/model/rank/extract.py

"""
Module: domain.extract.model.rank.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import ModelPrimeExtract, Rank, RankBlueprint
from transit import RankCarrier

T = TypeVar("T", bound="Rank")

class RankPrimeExtract(ModelPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for RankValidator.

    Attributes:
        carrier: RankCarrier
        blueprint: Optional[RankBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: RankCarrier[T],
            blueprint: Optional[RankBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: RankCarrier[T]
            blueprint: Optional[RankBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> RankCarrier[T]:
        return cast(RankCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[RankBlueprint[T]]:
        return cast(RankBlueprint, super().blueprint)