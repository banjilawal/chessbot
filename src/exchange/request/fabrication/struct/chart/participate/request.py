# src/exchange/request/fabrication/struct/chart/participate/request.py

"""
Module: exchange.request.fabrication.struct.chart.participate.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Participation
from exchange import ChartBuildRequest
from transit import Participation


class ParticipationBuildRequest(ChartBuildRequest[Participation]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a ParticipationValidator
            needs to run a job.

     Attributes:
         id: int
         item: StructCarrier[T]

     Provides:
     
     Super Class:
        ChartBuildRequest
     """
    
    def __init__(self, id: int, item: Participation):
        """
        Args:
            id: int
            item: Participation
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> Participation:
        return cast(Participation, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ParticipationBuildRequest):
            return self.id == other.id
        return False