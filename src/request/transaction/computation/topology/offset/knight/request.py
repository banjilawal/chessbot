# src/request/transaction/computation/topology/offset/knight/request.py

"""
Module: request.transaction.computation.topology.offset.knight.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from domain import Knight, Offset, Vector
from request import OffsetTopologyRequest


class KnightOffsetTopologyRequest(OffsetTopologyRequest[Knight]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: Vector
        offsets: VectorSet
        
     Provides:

     Super Class:
        OffsetTopologyRequest
     """
    
    def __init__(self, id: int, origin: Vector, offsets: VectorSet = Offset.KNIGHT.basis):
        """
        Args:
            id: int
            origin: Vector
            offsets: VectorSet
        """
        super().__init__(id=id, origin=origin, offsets=offsets)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, KnightOffsetTopologyRequest):
            return self.id == other.id
        return False