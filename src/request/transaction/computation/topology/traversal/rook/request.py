# src/request/transaction/computation/topology/traversal/rook/request.py

"""
Module: request.transaction.computation.topology.traversal.rook.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Rook, VectorNode
from request import TraversalTopologyRequest


class RookTraversalTopologyRequest(TraversalTopologyRequest[Rook]):
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
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RookTraversalTopologyRequest):
            return self.id == other.id
        return False