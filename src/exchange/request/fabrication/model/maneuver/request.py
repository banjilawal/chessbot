# src/exchange/request/fabrication/model/maneuver/request.py

"""
Module: exchange.request.fabrication.model.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Maneuver
from transit import ManeuverCarrier


class ManeuverBuildRequest(ModelBuildRequest[Maneuver]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Maneuver a build job.

     Attributes:
         id: int
         item: ManeuverCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: ManeuverCarrier):
        """
        Args:
            id: int
            item: ManeuverCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> ManeuverCarrier:
        return cast(ManeuverCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverBuildRequest):
            return self.id == other.id
        return False