# src/domain/metadata/null/model/rank/bishop/null.py

"""
Module: domain.metadata.null.model.rank.bishop.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Bishop, RankNullWarningSet
from err import (
    BishopBlueprintNullException, BishopCarrierNullException, BishopNullException
)


class BishopNullWarningSet(RankNullWarningSet[Bishop]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Bishop's integrity cycle.

    Attributes:
        model: BishopNullException
        carrier: BishopCarrierNullException
        blueprint: BishopBlueprintNullException

    Provides:

    Super Class:
        NullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[BishopNullException] | None = None,
            carrier: Optional[BishopCarrierNullException] | None = None,
            blueprint: Optional[BishopBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[BishopNullException]
            carrier: Optional[BishopCarrierNullException]
            blueprint: Optional[BishopBlueprintNullException]
        """
        super().__init__(
            model = model or BishopNullException(),
            carrier = carrier or BishopCarrierNullException(),
            blueprint = blueprint or BishopBlueprintNullException(),
        )
        
    @property
    def model(self) -> BishopNullException:
        return cast(BishopNullException, super().model)
    
    @property
    def carrier(self) -> BishopCarrierNullException:
        return cast(BishopCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BishopBlueprintNullException:
        return cast(BishopBlueprintNullException, super().blueprint)