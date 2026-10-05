# src/domain/metadata/nulls/struct/chart/walk/group.py

"""
Module: domain.metadata.nulls.struct.chart.walk.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartNullGroup, Walk
from err import (
    WalkBlueprintNullException, WalkCarrierNullException,
    WalkNullException
)


class WalkNullGroup(ChartNullGroup[Walk]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Walk's integrity cycle.

    Attributes:
        model: WalkNullException
        carrier: WalkCarrierNullException
        blueprint:WalkBlueprintNullException

    Provides:

    Super Class:
        ChartNullGroup
    """

    
    def __init__(
            self,
            model: Optional[WalkNullException] | None = None,
            carrier: Optional[WalkCarrierNullException] | None = None,
            blueprint: Optional[WalkBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[WalkNullException]
            carrier: Optional[WalkCarrierNullException]
            blueprint: Optional[WalkBlueprintNullException]
        """
        super().__init__(
            model=model or WalkNullException(),
            carrier=carrier or WalkCarrierNullException(),
            blueprint=blueprint or WalkBlueprintNullException(),
        )
        
    @property
    def struct(self) -> WalkNullException:
        return cast(WalkNullException, super().model)
    
    @property
    def model(self) -> WalkNullException:
        return self.struct
    
    @property
    def carrier(self) -> WalkCarrierNullException:
        return cast(WalkCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> WalkBlueprintNullException:
        return cast(WalkBlueprintNullException, super().blueprint)