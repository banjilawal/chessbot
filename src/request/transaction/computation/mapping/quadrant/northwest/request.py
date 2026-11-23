# src/request/transaction/computation/mapping/quadrant/northwest/request.py

"""
Module: request.transaction.computation.mapping.quadrant.northwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantStepFunction, VectorNode
from request import QuadrantProjectionRequest
from surface import NorthwestQuadrant


class NorthwestQuadrantMappingRequest(QuadrantProjectionRequest[NorthwestQuadrant]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        x_step: int
        slope: int

     Provides:

     Super Class:
        QuadrantMappingRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
            slope: int = QuadrantStepFunction.NORTHWEST.slope,
    ):
        """
        Args:
            id: int
            node: VectorNode
            x_step: int
            slope: int
        """
        super().__init__(id, node=node, x_step=x_step, slope=slope)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NorthwestQuadrantMappingRequest):
            return self.id == other.id
        return False