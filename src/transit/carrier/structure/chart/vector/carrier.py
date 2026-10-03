# src/transit/carrier/structure/chart/vector/carrier.py

"""
Module: transit.carrier.structure.chart.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorChart, VectorChartBlueprint
from transit import ChartCarrier


class VectorChartCarrier(ChartCarrier[VectorChart]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated VectorChart its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [VectorChart | VectorChartBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[VectorChartBlueprint]

    Super Class:
        ChartCarrier
    """
    
    _model: Optional[VectorChart]
    _blueprint: Optional[VectorChartBlueprint]
    
    def __init__(
            self,
            model: Optional[VectorChart] | None = None,
            blueprint: Optional[VectorChartBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[VectorChart]
            blueprint: Optional[VectorChartBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[VectorChart | VectorChartBlueprint]:
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
                isinstance(self._model, VectorChart)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, VectorChartBlueprint)
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
    
    def extract_blueprint(self) -> Optional[VectorChartBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        structure = cast(VectorChart, self._model)
        return VectorChartBlueprint(
            u=structure.u,
            v=structure.v,
        )


    