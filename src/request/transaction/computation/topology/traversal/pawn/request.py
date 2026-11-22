# src/request/transaction/computation/topology/traversal/pawn/request.py

"""
Module: request.transaction.computation.topology.traversal.pawn.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from collection import VectorSet
from domain import Pawn, Traversal, Vector
from request import TraversalTopologyRequest


class PawnTraversalTopologyRequest(TraversalTopologyRequest[Pawn]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: Vector
        traversals: VectorSet
        
     Provides:

     Super Class:
        TraversalTopologyRequest
     """
    
    def __init__(self, id: int, origin: Vector, traversals: VectorSet = Traversal.PAWN.basis):
        """
        Args:
            id: int
            origin: Vector
            traversals: VectorSet
        """
        super().__init__(id=id, origin=origin, traversals=traversals)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PawnTraversalTopologyRequest):
            return self.id == other.id
        return False