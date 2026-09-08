# src/domain/metadata/nulls/model/rank/queen/group.py

"""
Module: domain.metadata.nulls.model.rank.queen.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RankNullGroup
from err import QueenBlueprintNullException, QueenCarrierNullException, QueenNullException


class QueenNullGroup(RankNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a QueenRank's integrity cycle.

    Attributes:
        model: QueenNullException
        carrier: QueenCarrierNullException
        blueprint: QueenBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[QueenNullException] | None = None,
            carrier: Optional[QueenCarrierNullException] | None = None,
            blueprint: Optional[QueenBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[QueenNullException]
            carrier: Optional[QueenCarrierNullException]
            blueprint: Optional[QueenBlueprintNullException]
        """
        super().__init__(
            model = model or QueenNullException(),
            carrier = carrier or QueenCarrierNullException(),
            blueprint = blueprint or QueenBlueprintNullException(),
        )
        
    @property
    def model(self) -> QueenNullException:
        return cast(QueenNullException, super().model)
    
    @property
    def carrier(self) -> QueenCarrierNullException:
        return cast(QueenCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> QueenBlueprintNullException:
        return cast(QueenBlueprintNullException, super().blueprint)