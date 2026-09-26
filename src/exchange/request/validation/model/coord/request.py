# src/exchange/request/validation/model/coord/request.py

"""
Module: exchange.request.validation.model.coord.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from exchange import ModelValidationRequest
from domain import Coord
from transit import CoordCarrier


class CoordValidationRequest(ModelValidationRequest[Coord]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Coord a validation job.

     Attributes:
         id: int
         item: CoordCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: CoordCarrier):
        """
        Args:
            id: int
            item: CoordCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> CoordCarrier:
        return cast(CoordCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CoordValidationRequest):
            return self.id == other.id
        return False