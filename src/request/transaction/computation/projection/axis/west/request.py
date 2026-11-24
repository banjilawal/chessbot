# src/request/transaction/computation/projection/axis/west/request.py

"""
Module: request.transaction.computation.projection.axis.west.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDelta, Vector, VectorNode
from request import AxisProjectionRequest
from surface import WestAxis


class WestAxisProjectionRequest(AxisProjectionRequest[WestAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        delta: Vector
        
     Provides:

     Super Class:
        AxisProjectionRequest
     """
    
    def __init__(self, id: int, node: VectorNode, delta: Vector = AxisDelta.WEST.vector):
        """
        Args:
            id: int
            node: VectorNode
            delta: Vector
        """
        super().__init__(id=id, node=node, delta=delta)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, WestAxisProjectionRequest):
            return self.id == other.id
        return False