# src/exchange/request/validation/struct/chart/token/request.py

"""
Module: exchange.request.validation.struct.chart.token.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import TokenChart
from exchange import ChartValidationRequest
from transit import TokenChartCarrier


class TokenChartValidationRequest(ChartValidationRequest[TokenChart]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a TokenChartValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        ChartValidationRequest
     """
    
    def __init__(self, id: int, item: TokenChartCarrier):
        """
        Args:
            id: int
            item: TokenChart
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> TokenChartCarrier:
        return cast(TokenChartCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChartValidationRequest):
            return self.id == other.id
        return False