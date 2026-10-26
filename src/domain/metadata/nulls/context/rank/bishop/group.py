# src/domain/metadata/nulls/context/rank/bishop/group.py

"""
Module: domain.metadata.nulls.context.rank.bishop.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, RankContextNullGroup
from err import (
    BishopContextBlueprintNullException, BishopContextCarrierNullException, BishopContextNullException
)


class BishopContextNullGroup(RankContextNullGroup[BishopContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Bishop's integrity cycle.

    Attributes:
        context: BishopContextNullException
        carrier: BishopContextCarrierNullException
        blueprint: BishopContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[BishopContextNullException] | None = None,
            carrier: Optional[BishopContextCarrierNullException] | None = None,
            blueprint: Optional[BishopContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[BishopContextNullException]
            carrier: Optional[BishopContextCarrierNullException]
            blueprint: Optional[BishopContextBlueprintNullException]
        """
        super().__init__(
            context = context or BishopContextNullException(),
            carrier = carrier or BishopContextCarrierNullException(),
            blueprint = blueprint or BishopContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> BishopContextNullException:
        return cast(BishopContextNullException, super().context)
    
    @property
    def carrier(self) -> BishopContextCarrierNullException:
        return cast(BishopContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BishopContextBlueprintNullException:
        return cast(BishopContextBlueprintNullException, super().blueprint)