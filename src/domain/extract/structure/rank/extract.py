# src/domain/extract/struct/rank/extract.py

"""
Module: domain.extract.struct.rank.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import Blueprint, StructPrimeExtract, Rank, RankBlueprint
from transit import RankCarrier

T = TypeVar("T", bound="Rank")

class RankPrimeExtract(StructPrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for RankValidator.

    Attributes:
        carrier: RankCarrier
        blueprint: Optional[RankBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
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
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> RankCarrier[T]:
        return cast(RankCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[RankBlueprint[T]]:
        return cast(RankBlueprint, super().blueprint)