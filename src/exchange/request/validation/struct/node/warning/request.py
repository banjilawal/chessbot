# src/exchange/request/validation/struct/node/warning/request.py

"""
Module: exchange.request.validation.struct.node.warning.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import WarningNode
from exchange import NodeValidationRequest
from transit import WarningNodeCarrier


class EncounterWarningNodeValidationRequest(NodeValidationRequest[WarningNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a WarningNodeValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        NodeValidationRequest
     """
    
    def __init__(self, id: int, item: WarningNodeCarrier):
        """
        Args:
            id: int
            item: WarningNode
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> WarningNodeCarrier:
        return cast(WarningNodeCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeValidationRequest):
            return self.id == other.id
        return False