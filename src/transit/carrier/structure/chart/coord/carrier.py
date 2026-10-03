# src/transit/carrier/structure/chart/coord/carrier.py

"""
Module: transit.carrier.structure.chart.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordChart, CoordChartBlueprint
from transit import ChartCarrier


class CoordChartCarrier(ChartCarrier[CoordChart]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CoordChart its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [CoordChart | CoordChartBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CoordChartBlueprint]

    Super Class:
        ChartCarrier
    """
    
    _model: Optional[CoordChart]
    _blueprint: Optional[CoordChartBlueprint]
    
    def __init__(
            self,
            model: Optional[CoordChart] | None = None,
            blueprint: Optional[CoordChartBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CoordChart]
            blueprint: Optional[CoordChartBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CoordChart | CoordChartBlueprint]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, CoordChart)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, CoordChartBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[CoordChartBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        structure = cast(CoordChart, self._model)
        return CoordChartBlueprint(
            origin=structure.origin,
            terminus=structure.terminus,
        )


    