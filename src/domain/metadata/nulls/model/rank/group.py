# src/domain/metadata/nulls/model/rank/group.py

"""
Module: domain.metadata.nulls.model.rank.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import NullExceptionGroup, Rank
from err import (
    RankBlueprintNullException, RankCarrierNullException, RankNullException
)

T = TypeVar("T", bound="Rank")

class RankNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Rank's integrity cycle.

    Attributes:
        model: RankNullException
        carrier: RankCarrierNullException
        blueprint: RankBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[RankNullException] | None = None,
            carrier: Optional[RankCarrierNullException] | None = None,
            blueprint: Optional[RankBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[RankNullException]
            carrier: Optional[RankCarrierNullException]
            blueprint: Optional[RankBlueprintNullException]
        """
        super().__init__(
            model = model or RankNullException(),
            carrier = carrier or RankCarrierNullException(),
            blueprint = blueprint or RankBlueprintNullException(),
        )
        
    @property
    def model(self) -> RankNullException:
        return cast(RankNullException, super().model)
    
    @property
    def carrier(self) -> RankCarrierNullException:
        return cast(RankCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> RankBlueprintNullException:
        return cast(RankBlueprintNullException, super().blueprint)