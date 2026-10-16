# src/exchange/request/fabrication/model/alert/request.py

"""
Module: exchange.request.fabrication.model.alert.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Alert
from transit import AlertCarrier


class AlertBuildRequest(ModelBuildRequest[Alert]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Alert a build job.

     Attributes:
         id: int
         item: AlertCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: AlertCarrier):
        """
        Args:
            id: int
            item: AlertCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> AlertCarrier:
        return cast(AlertCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AlertBuildRequest):
            return self.id == other.id
        return False