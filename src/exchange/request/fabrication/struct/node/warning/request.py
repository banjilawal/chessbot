# src/exchange/request/fabrication/struct/node/warning/request.py

"""
Module: exchange.request.fabrication.struct.node.warning.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import WarningNode
from exchange import NodeBuildRequest
from transit import WarningNode


class EncounterWarningNodeBuildRequest(NodeBuildRequest[WarningNode]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Transport the collection and other objects a WarningNodeValidator
            needs to run a job.

     Attributes:
         id: int
         item: StructCarrier[T]

     Provides:
     
     Super Class:
        NodeBuildRequest
     """
    
    def __init__(self, id: int, item: WarningNode):
        """
        Args:
            id: int
            item: WarningNode
        """
        super().__init__(id=id, item=item)
    
    @property
    def item(self) -> WarningNode:
        return cast(WarningNode, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeBuildRequest):
            return self.id == other.id
        return False