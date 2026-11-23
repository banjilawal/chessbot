# src/request/transaction/computation/sequence/quadrant/southeast/request.py

"""
Module: request.transaction.computation.sequence.quadrant.southeast.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantDestination, QuadrantStepFunction, Vector, VectorNode
from request import QuadrantSequenceRequest
from surface import SoutheastQuadrant


class SoutheastQuadrantSequenceRequest(QuadrantSequenceRequest[SoutheastQuadrant]):
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
        QuadrantSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            x_step: int = QuadrantStepFunction.SOUTHEAST.x_step,
            slope: int = QuadrantStepFunction.SOUTHEAST.slope,
            terminus: Vector = QuadrantDestination.SOUTHEAST.vector,
    ):
        """
        Args:
            id: int
            node: VectorNode
            x_step: int
            slope: int
            terminus: Vector
        """
        super().__init__(id, node=node, x_step=x_step, slope=slope, terminus=terminus)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SoutheastQuadrantSequenceRequest):
            return self.id == other.id
        return False