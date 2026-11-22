# src/request/transaction/computation/mapping/axis/north/request.py

"""
Module: request.transaction.computation.mapping.axis.north.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import AxisDelta, Vector
from request import AxisMappingRequest
from surface import NorthAxis


class NorthAxisMappingRequest(AxisMappingRequest[NorthAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        vector: Vector
        delta: Vector
        
     Provides:

     Super Class:
        AxisMappingRequest
     """
    
    def __init__(self, id: int, vector: Vector, delta: Vector = AxisDelta.NORTH.vector):
        """
        Args:
            id: int
            vector: Vector
            delta: Vector
        """
        super().__init__(id=id, vector=vector, delta=delta)
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NorthAxisMappingRequest):
            return self.id == other.id
        return False