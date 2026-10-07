# src/exchange/request/validation/model/footstep/request.py

"""
Module: exchange.request.validation.model.footstep.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import Footstep
from exchange import ModelValidationRequest
from transit import FootstepCarrier


class FootstepValidationRequest(ModelValidationRequest[Footstep]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a FootstepValidator
            needs to run a job.

     Attributes:
         id: int
         item: FootstepCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: FootstepCarrier):
        """
        Args:
            id: int
            item: FootstepCarrier
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> FootstepCarrier:
        return cast(FootstepCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, FootstepValidationRequest):
            return self.id == other.id
        return False