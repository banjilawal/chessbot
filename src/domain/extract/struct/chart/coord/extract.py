# src/domain/extract/struct/chart/walk.extract.py

"""
Module: domain.extract.struct.chart.walk.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Walk, WalkBlueprint, ChartPrimeExtract
from transit import WalkCarrier


class WalkPrimeExtract(ChartPrimeExtract[Walk]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for WalkValidator.

    Attributes:
        carrier: WalkCarrier
        blueprint: Optional[WalkBlueprint]

    Provides:

    Super Class:
        ChartPrimeExtract
    """

    def __init__(
            self,
            reference: WalkCarrier,
            safe_blueprint: Optional[WalkBlueprint] | None = None,
    ):
        """
        Args:
            reference: WalkCarrier
            safe_blueprint: Optional[WalkBlueprint]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> WalkCarrier:
        return cast(WalkCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[WalkBlueprint]:
        return cast(WalkBlueprint, super().blueprint)