# src/exchange/request/validation/model/encounter/request.py

"""
Module: exchange.request.validation.model.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelValidationRequest
from domain import Encounter
from transit import EncounterCarrier


class EncounterValidationRequest(ModelValidationRequest[Encounter]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Encounter a validation job.

     Attributes:
         id: int
         item: EncounterCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
     """
    
    def __init__(self, id: int, item: EncounterCarrier):
        """
        Args:
            id: int
            item: EncounterCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> EncounterCarrier:
        return cast(EncounterCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EncounterValidationRequest):
            return self.id == other.id
        return False