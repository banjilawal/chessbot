# src/domain/metadata/nulls/model/rank/king/group.py

"""
Module: domain.metadata.nulls.model.rank.king.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import King, RankNullGroup
from err import (
    KingBlueprintNullException, KingCarrierNullException, KingNullException
)


class KingNullGroup(RankNullGroup[King]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a King's integrity cycle.

    Attributes:
        model: KingNullException
        carrier: KingCarrierNullException
        blueprint: KingBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KingNullException] | None = None,
            carrier: Optional[KingCarrierNullException] | None = None,
            blueprint: Optional[KingBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KingNullException]
            carrier: Optional[KingCarrierNullException]
            blueprint: Optional[KingBlueprintNullException]
        """
        super().__init__(
            model = model or KingNullException(),
            carrier = carrier or KingCarrierNullException(),
            blueprint = blueprint or KingBlueprintNullException(),
        )
        
    @property
    def model(self) -> KingNullException:
        return cast(KingNullException, super().model)
    
    @property
    def carrier(self) -> KingCarrierNullException:
        return cast(KingCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KingBlueprintNullException:
        return cast(KingBlueprintNullException, super().blueprint)