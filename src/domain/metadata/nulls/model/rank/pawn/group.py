# src/domain/metadata/nulls/model/rank/pawn/group.py

"""
Module: domain.metadata.nulls.model.rank.pawn.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Pawn, RankNullGroup
from err import (
    PawnBlueprintNullException, PawnCarrierNullException, PawnNullException
)


class PawnNullGroup(RankNullGroup[Pawn]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Pawn's integrity cycle.

    Attributes:
        model: PawnNullException
        carrier: PawnCarrierNullException
        blueprint: PawnBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[PawnNullException] | None = None,
            carrier: Optional[PawnCarrierNullException] | None = None,
            blueprint: Optional[PawnBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PawnNullException]
            carrier: Optional[PawnCarrierNullException]
            blueprint: Optional[PawnBlueprintNullException]
        """
        super().__init__(
            model = model or PawnNullException(),
            carrier = carrier or PawnCarrierNullException(),
            blueprint = blueprint or PawnBlueprintNullException(),
        )
        
    @property
    def model(self) -> PawnNullException:
        return cast(PawnNullException, super().model)
    
    @property
    def carrier(self) -> PawnCarrierNullException:
        return cast(PawnCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PawnBlueprintNullException:
        return cast(PawnBlueprintNullException, super().blueprint)