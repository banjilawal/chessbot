# src/domain/metadata/nulls/context/rank/group.py

"""
Module: domain.metadata.nulls.context.rank.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import ContextNullGroup, Rank
from err import (
    RankContextBlueprintNullException, RankContextCarrierNullException, RankContextNullException
)

T = TypeVar("T", bound="Rank")

class RankContextNullGroup(ContextNullGroup[T], ABC, Generic[TContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Rank's integrity cycle.

    Attributes:
        context: RankContextNullException
        carrier: RankContextCarrierNullException
        blueprint: RankContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[RankContextNullException] | None = None,
            carrier: Optional[RankContextCarrierNullException] | None = None,
            blueprint: Optional[RankContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[RankContextNullException]
            carrier: Optional[RankContextCarrierNullException]
            blueprint: Optional[RankContextBlueprintNullException]
        """
        super().__init__(
            context = context or RankContextNullException(),
            carrier = carrier or RankContextCarrierNullException(),
            blueprint = blueprint or RankContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> RankContextNullException:
        return cast(RankContextNullException, super().context)
    
    @property
    def carrier(self) -> RankContextCarrierNullException:
        return cast(RankContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> RankContextBlueprintNullException:
        return cast(RankContextBlueprintNullException, super().blueprint)