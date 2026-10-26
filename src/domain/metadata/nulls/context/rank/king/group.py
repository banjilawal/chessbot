# src/domain/metadata/nulls/context/rank/king/group.py

"""
Module: domain.metadata.nulls.context.rank.king.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import King, RankContextNullGroup
from err import (
    KingContextBlueprintNullException, KingContextCarrierNullException, KingContextNullException
)


class KingContextNullGroup(RankContextNullGroup[KingContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a King's integrity cycle.

    Attributes:
        context: KingContextNullException
        carrier: KingContextCarrierNullException
        blueprint: KingContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[KingContextNullException] | None = None,
            carrier: Optional[KingContextCarrierNullException] | None = None,
            blueprint: Optional[KingContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[KingContextNullException]
            carrier: Optional[KingContextCarrierNullException]
            blueprint: Optional[KingContextBlueprintNullException]
        """
        super().__init__(
            context = context or KingContextNullException(),
            carrier = carrier or KingContextCarrierNullException(),
            blueprint = blueprint or KingContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> KingContextNullException:
        return cast(KingContextNullException, super().context)
    
    @property
    def carrier(self) -> KingContextCarrierNullException:
        return cast(KingContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KingContextBlueprintNullException:
        return cast(KingContextBlueprintNullException, super().blueprint)