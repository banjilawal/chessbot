# src/exchange/request/validation/context/maneuver/request.py

"""
Module: exchange.request.validation.context.maneuver.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Maneuver
from transit import ManeuverContextCarrier


class ManeuverContextValidationRequest(ContextValidationRequest[ManeuverContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a ManeuverContextValidator job details.

     Attributes:
         id: int
         item: ManeuverContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: ManeuverContextCarrier):
        """
        Args:
            id: int
            item: ManeuverContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> ManeuverContextCarrier:
        return cast(ManeuverContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ManeuverContextValidationRequest):
            return self.id == other.id
        return False