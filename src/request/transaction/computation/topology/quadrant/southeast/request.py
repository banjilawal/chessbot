# src/request/transaction/computation/topology/quadrant/southeast/request.py

"""
Module: request.transaction.computation.topology.quadrant.southeast.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantStepFunction, Vector
from request import QuadrantTopologyRequest
from surface import SoutheastQuadrant


class SoutheastQuadrantTopologyRequest(QuadrantTopologyRequest[SoutheastQuadrant]):
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
        QuadrantTopologyRequest
     """
    
    def __init__(
            self,
            id: int,
            vector: Vector,
            x_step: int = QuadrantStepFunction.SOUTHEAST.x_step,
            slope: int = QuadrantStepFunction.SOUTHEAST.slope,
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
        if isinstance(other, SoutheastQuadrantTopologyRequest):
            return self.id == other.id
        return False