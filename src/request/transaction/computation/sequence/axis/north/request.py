# src/request/transaction/computation/sequence/axis/north/request.py

"""
Module: request.transaction.computation.sequence.axis.north.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDelta, AxisDestination, Vector, VectorNode
from request import AxisSequenceRequest
from surface import NorthAxis


class NorthAxisSequenceRequest(AxisSequenceRequest[NorthAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        delta: Vector
        terminus: Vector
        
     Provides:

     Super Class:
        AxisVectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            delta: Vector = AxisDelta.NORTH.vector,
            terminus: Vector = AxisDestination.NORTH.vector,
    ):
        """
        Args:
            id: int
            node: VectorNode
            delta: Vector
            terminus: Vector
        """
        super().__init__(id=id, node=node, delta=delta, terminus=terminus)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NorthAxisSequenceRequest):
            return self.id == other.id
        return False