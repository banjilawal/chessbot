# src/transit/carrier/structure/chart/square/carrier.py

"""
Module: transit.carrier.structure.chart.square.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import SquareChart, SquareChartBlueprint
from transit import ChartCarrier


class SquareChartCarrier(ChartCarrier[SquareChart]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated SquareChart its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [SquareChart | SquareChartBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[SquareChartBlueprint]

    Super Class:
        ChartCarrier
    """
    
    _model: Optional[SquareChart]
    _blueprint: Optional[SquareChartBlueprint]
    
    def __init__(
            self,
            model: Optional[SquareChart] | None = None,
            blueprint: Optional[SquareChartBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SquareChart]
            blueprint: Optional[SquareChartBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[SquareChart | SquareChartBlueprint]:
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
                isinstance(self._model, SquareChart)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, SquareChartBlueprint)
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
    
    def extract_blueprint(self) -> Optional[SquareChartBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        structure = cast(SquareChart, self._model)
        return SquareChartBlueprint(
            origin=structure.origin,
            destination=structure.destination,
        )


    