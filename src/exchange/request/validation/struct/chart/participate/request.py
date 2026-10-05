# src/exchange/request/validation/struct/chart/participate/request.py

"""
Module: exchange.request.validation.struct.chart.participate.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Participation
from exchange import ChartValidationRequest
from transit import ParticipationCarrier


class ParticipationValidationRequest(ChartValidationRequest[Participation]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a ParticipationValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        ChartValidationRequest
     """
    
    def __init__(self, id: int, item: ParticipationCarrier):
        """
        Args:
            id: int
            item: Participation
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> ParticipationCarrier:
        return cast(ParticipationCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ParticipationValidationRequest):
            return self.id == other.id
        return False