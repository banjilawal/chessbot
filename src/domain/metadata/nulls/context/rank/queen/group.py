# src/domain/metadata/nulls/context/rank/queen/group.py

"""
Module: domain.metadata.nulls.context.rank.queen.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Queen, RankContextNullGroup
from err import (
    QueenContextBlueprintNullException, QueenContextCarrierNullException, QueenContextNullException
)


class QueenContextNullGroup(RankContextNullGroup[QueenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Queen's integrity cycle.

    Attributes:
        context: QueenContextNullException
        carrier: QueenContextCarrierNullException
        blueprint: QueenContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[QueenContextNullException] | None = None,
            carrier: Optional[QueenContextCarrierNullException] | None = None,
            blueprint: Optional[QueenContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[QueenContextNullException]
            carrier: Optional[QueenContextCarrierNullException]
            blueprint: Optional[QueenContextBlueprintNullException]
        """
        super().__init__(
            context = context or QueenContextNullException(),
            carrier = carrier or QueenContextCarrierNullException(),
            blueprint = blueprint or QueenContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> QueenContextNullException:
        return cast(QueenContextNullException, super().context)
    
    @property
    def carrier(self) -> QueenContextCarrierNullException:
        return cast(QueenContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> QueenContextBlueprintNullException:
        return cast(QueenContextBlueprintNullException, super().blueprint)