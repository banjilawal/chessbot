# src/request/transaction/computation/sequence/quadrant/northwest/request.py

"""
Module: request.transaction.computation.sequence.quadrant.northwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import QuadrantDestination, QuadrantStepFunction, Vector, VectorNode
from request import QuadrantSequenceRequest
from surface import NorthwestQuadrant


class NorthwestQuadrantSequenceRequest(QuadrantSequenceRequest[NorthwestQuadrant]):
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
            x_step: int = QuadrantStepFunction.NORTHWEST.x_step,
            slope: int = QuadrantStepFunction.NORTHWEST.slope,
            terminus: Vector = QuadrantDestination.NORTHWEST.vector,
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
        if isinstance(other, NorthwestQuadrantSequenceRequest):
            return self.id == other.id
        return False