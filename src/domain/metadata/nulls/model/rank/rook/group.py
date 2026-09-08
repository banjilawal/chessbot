# src/domain/metadata/nulls/model/rank/rook/group.py

"""
Module: domain.metadata.nulls.model.rank.rook.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RankNullGroup
from err import RookBlueprintNullException, RookCarrierNullException, RookNullException


class RookNullGroup(RankNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a RookRank's integrity cycle.

    Attributes:
        model: RookNullException
        carrier: RookCarrierNullException
        blueprint: RookBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[RookNullException] | None = None,
            carrier: Optional[RookCarrierNullException] | None = None,
            blueprint: Optional[RookBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[RookNullException]
            carrier: Optional[RookCarrierNullException]
            blueprint: Optional[RookBlueprintNullException]
        """
        super().__init__(
            model = model or RookNullException(),
            carrier = carrier or RookCarrierNullException(),
            blueprint = blueprint or RookBlueprintNullException(),
        )
        
    @property
    def model(self) -> RookNullException:
        return cast(RookNullException, super().model)
    
    @property
    def carrier(self) -> RookCarrierNullException:
        return cast(RookCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> RookBlueprintNullException:
        return cast(RookBlueprintNullException, super().blueprint)