# src/exchange/request/validation/structure/chart/request.py

"""
Module: exchange.request.validation.structure.chart.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Chart
from exchange import StructureValidationRequest
from transit import ChartCarrier

T = TypeVar("T", bound="Chart")


class ChartValidationRequest(StructureValidationRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a ChartValidator needs to run a job.

     Attributes:
         id: int
         item: T

     Provides:
     
     Super Class:
        ValidationRequest
     """
    
    def __init__(self, id: int, item: ChartCarrier[T]):
        """
        Args:
            id: int
            item: ChartCarrier[T]
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> ChartCarrier[T]:
        return cast(ChartCarrier[T], super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ChartValidationRequest):
            return self.id == other.id
        return False