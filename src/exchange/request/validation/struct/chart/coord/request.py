# src/exchange/request/validation/struct/chart/coord/request.py

"""
Module: exchange.request.validation.struct.chart.coord.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import CoordChart
from exchange import ChartValidationRequest
from transit import CoordChartCarrier


class CoordChartValidationRequest(ChartValidationRequest[CoordChart]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a CoordChartValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        ChartValidationRequest
     """
    
    def __init__(self, id: int, item: CoordChartCarrier):
        """
        Args:
            id: int
            item: CoordChart
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> CoordChartCarrier:
        return cast(CoordChartCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChartValidationRequest):
            return self.id == other.id
        return False