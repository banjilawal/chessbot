# src/request/transaction/computation/topology/traversal/bishop/request.py

"""
Module: request.transaction.computation.topology.traversal.bishop.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from domain import Bishop, VectorNode
from request import (
    NortheastQuadrantSequenceRequest, NorthwestQuadrantSequenceRequest,
    SoutheastQuadrantSequenceRequest, SouthwestQuadrantSequenceRequest, TraversalTopologyRequest
)


class BishopTraversalTopologyRequest(TraversalTopologyRequest[Bishop]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: VectorNode
        
     Provides:

     Super Class:
        TraversalTopologyRequest
     """
    
    def __init__(self, id: int, origin: VectorNode):
        """
        Args:
            id: int
            origin: VectorNode
        """
        super().__init__(id=id, origin=origin)
        
    @property
    def northeast_request(self) -> NortheastQuadrantSequenceRequest:
        return NortheastQuadrantSequenceRequest(id=self.id, node=self.origin)
    
    @property
    def northwest_request(self) -> NorthwestQuadrantSequenceRequest:
        return NorthwestQuadrantSequenceRequest(id=self.id, node=self.origin)
    
    @property
    def southeast_request(self) -> SoutheastQuadrantSequenceRequest:
        return SoutheastQuadrantSequenceRequest(id=self.id, node=self.origin)
    
    @property
    def southwest_request(self) -> SouthwestQuadrantSequenceRequest:
        return SouthwestQuadrantSequenceRequest(id=self.id, node=self.origin)
    
    @property
    def sequence_requests(self) -> list:
        return [self.northeast_request, self.northwest_request, self.southeast_request, self.southwest_request]
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, BishopTraversalTopologyRequest):
            return self.id == other.id
        return False