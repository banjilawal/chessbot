# src/exchange/request/validation/context/encounter/request.py

"""
Module: exchange.request.validation.context.encounter.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ContextValidationRequest
from domain import Encounter
from transit import EncounterContextCarrier


class EncounterContextValidationRequest(ContextValidationRequest[EncounterContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide a EncounterContextValidator job details.

     Attributes:
         id: int
         item: EncounterContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: EncounterContextCarrier):
        """
        Args:
            id: int
            item: EncounterContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> EncounterContextCarrier:
        return cast(EncounterContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EncounterContextValidationRequest):
            return self.id == other.id
        return False