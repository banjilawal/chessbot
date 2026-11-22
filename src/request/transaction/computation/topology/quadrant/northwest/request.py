# src/request/transaction/computation/topology/quadrant/northwest/request.py

"""
Module: request.transaction.computation.topology.quadrant.northwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantStepFunction, Vector
from request import QuadrantTopologyRequest
from surface import NorthwestQuadrant


class NorthwestQuadrantTopologyRequest(QuadrantTopologyRequest[NorthwestQuadrant]):
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
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
            slope: int = QuadrantStepFunction.NORTHWEST.slope,
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
        if isinstance(other, NorthwestQuadrantTopologyRequest):
            return self.id == other.id
        return False