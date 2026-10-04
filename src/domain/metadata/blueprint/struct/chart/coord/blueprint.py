# src/domain/metadata/blueprint/struct/chart/coord.blueprint.py

"""
Module: domain.metadata.blueprint.struct.chart.coord.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Coord, ChartBlueprint, CoordChart
from err import CoordChartNullException


class CoordChartBlueprint(ChartBlueprint[CoordChart]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a CoordChart.

     Attributes:
        position: Optional[Coord]
        previous_position: Optional[Coord]
        Optional[Type[CoordChart]]
        domain_null_exception: Optional[CoordChartNullException]

     Provides:

     Super Class:
        ChartBlueprint
     """
    _position: Optional[Coord]
    _previous_position: Optional[Coord]
    
    def __init__(
            self,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            domain_class: Optional[Type[CoordChart]] | None = None,
            domain_null_exception: Optional[CoordChartNullException] | None = None,
    ):
        """
        Args:
            position: Optional[Coord]
            previous_position: Optional[Coord]
            Optional[Type[CoordChart]]
            domain_null_exception: Optional[CoordChartNullException]
        """
        super().__init__(
            domain_class=domain_class or CoordChart,
            domain_null_exception=domain_null_exception or CoordChartNullException(),
        )
        self._position = position
        self._previous_position = previous_position
        
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
    @property
    def domain_class(self) -> Type[CoordChart]:
        return cast(Type[CoordChart], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CoordChartNullException:
        return cast(CoordChartNullException, super().domain_null_exception)
    
    
