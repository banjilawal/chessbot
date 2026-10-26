# src/domain/metadata/nulls/context/rank/pawn/group.py

"""
Module: domain.metadata.nulls.context.rank.pawn.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Pawn, RankContextNullGroup
from err import (
    PawnContextBlueprintNullException, PawnContextCarrierNullException, PawnContextNullException
)


class PawnContextNullGroup(RankContextNullGroup[PawnContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Pawn's integrity cycle.

    Attributes:
        context: PawnContextNullException
        carrier: PawnContextCarrierNullException
        blueprint: PawnContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[PawnContextNullException] | None = None,
            carrier: Optional[PawnContextCarrierNullException] | None = None,
            blueprint: Optional[PawnContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[PawnContextNullException]
            carrier: Optional[PawnContextCarrierNullException]
            blueprint: Optional[PawnContextBlueprintNullException]
        """
        super().__init__(
            context = context or PawnContextNullException(),
            carrier = carrier or PawnContextCarrierNullException(),
            blueprint = blueprint or PawnContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> PawnContextNullException:
        return cast(PawnContextNullException, super().context)
    
    @property
    def carrier(self) -> PawnContextCarrierNullException:
        return cast(PawnContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PawnContextBlueprintNullException:
        return cast(PawnContextBlueprintNullException, super().blueprint)