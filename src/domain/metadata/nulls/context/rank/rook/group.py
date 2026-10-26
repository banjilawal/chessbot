# src/domain/metadata/nulls/context/rank/rook/group.py

"""
Module: domain.metadata.nulls.context.rank.rook.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RankContextNullGroup, Rook
from err import (
    RookContextBlueprintNullException, RookContextCarrierNullException, RookContextNullException
)


class RookContextNullGroup(RankContextNullGroup[RookContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Rook's integrity cycle.

    Attributes:
        context: RookContextNullException
        carrier: RookContextCarrierNullException
        blueprint: RookContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[RookContextNullException] | None = None,
            carrier: Optional[RookContextCarrierNullException] | None = None,
            blueprint: Optional[RookContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[RookContextNullException]
            carrier: Optional[RookContextCarrierNullException]
            blueprint: Optional[RookContextBlueprintNullException]
        """
        super().__init__(
            context = context or RookContextNullException(),
            carrier = carrier or RookContextCarrierNullException(),
            blueprint = blueprint or RookContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> RookContextNullException:
        return cast(RookContextNullException, super().context)
    
    @property
    def carrier(self) -> RookContextCarrierNullException:
        return cast(RookContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> RookContextBlueprintNullException:
        return cast(RookContextBlueprintNullException, super().blueprint)