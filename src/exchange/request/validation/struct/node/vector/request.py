# src/exchange/request/validation/struct/node/vector/request.py

"""
Module: exchange.request.validation.struct.node.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import VectorNode
from exchange import NodeValidationRequest
from transit import VectorNodeCarrier


class VectorNodeValidationRequest(NodeValidationRequest[VectorNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a VectorNodeValidator
            needs to run a job.

     Attributes:
         id: int
         item: Any

     Provides:
     
     Super Class:
        NodeValidationRequest
     """
    
    def __init__(self, id: int, item: VectorNodeCarrier):
        """
        Args:
            id: int
            item: VectorNode
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> VectorNodeCarrier:
        return cast(VectorNodeCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeValidationRequest):
            return self.id == other.id
        return False