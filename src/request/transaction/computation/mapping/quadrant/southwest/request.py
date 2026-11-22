# src/request/transaction/computation/mapping/quadrant/southwest/request.py

"""
Module: request.transaction.computation.mapping.quadrant.southwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantStepFunction, Vector
from request import QuadrantMappingRequest


class SouthwestQuadrantMappingRequest(QuadrantMappingRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        vector: Vector
        x_step: int
        slope: int

     Provides:

     Super Class:
        QuadrantMappingRequest
     """
    
    def __init__(
            self,
            id: int,
            vector: Vector,
            x_step: int = QuadrantStepFunction.SOUTHWEST.x_step,
            slope: int = QuadrantStepFunction.SOUTHWEST.slope,
    ):
        """
        Args:
            id: int
            vector: Vector
            x_step: int
            slope: int
        """
        super().__init__(id, vector=vector, x_step=x_step, slope=slope)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SouthwestQuadrantMappingRequest):
            return self.id == other.id
        return False