# src/domain/metadata/nulls/model/rank/knight/group.py

"""
Module: domain.metadata.nulls.model.rank.knight.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RankNullGroup
from err import KnightBlueprintNullException, KnightCarrierNullException, KnightNullException


class KnightNullGroup(RankNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a KnightRank's integrity cycle.

    Attributes:
        model: KnightNullException
        carrier: KnightCarrierNullException
        blueprint: KnightBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KnightNullException] | None = None,
            carrier: Optional[KnightCarrierNullException] | None = None,
            blueprint: Optional[KnightBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KnightNullException]
            carrier: Optional[KnightCarrierNullException]
            blueprint: Optional[KnightBlueprintNullException]
        """
        super().__init__(
            model = model or KnightNullException(),
            carrier = carrier or KnightCarrierNullException(),
            blueprint = blueprint or KnightBlueprintNullException(),
        )
        
    @property
    def model(self) -> KnightNullException:
        return cast(KnightNullException, super().model)
    
    @property
    def carrier(self) -> KnightCarrierNullException:
        return cast(KnightCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KnightBlueprintNullException:
        return cast(KnightBlueprintNullException, super().blueprint)