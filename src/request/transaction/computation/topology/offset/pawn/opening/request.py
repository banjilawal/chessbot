# src/request/transaction/computation/topology/offset/pawn/request.py

"""
Module: request.transaction.computation.topology.offset.pawn.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from domain import Offset, VectorNode
from request import PawnTopologyRequest


class OpeningPawnTopologyRequest(PawnTopologyRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: VectorNode
        offsets: VectorSet
        
     Provides:

     Super Class:
        PawnTopologyRequest
     """
    
    def __init__(self, id: int, origin: VectorNode, offsets: VectorSet):
        """
        Args:
            id: int
            origin: VectorNode
            offsets: VectorSet
        """
        super().__init__(id=id, origin=origin, offsets=offsets)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OpeningPawnTopologyRequest):
            return self.id == other.id
        return False