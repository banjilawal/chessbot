# src/request/transaction/computation/sequence/quadrant/northwest/request.py

"""
Module: request.transaction.computation.sequence.quadrant.northwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import QuadrantDestination, QuadrantStepFunction, Vector, VectorNode
from operation import NorthwestQuadrantNodeStepper
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
        terminus: Vector
        step_function: NorthwestQuadrantNodeStepper

     Provides:

     Super Class:
        QuadrantSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = QuadrantDestination.NORTHWEST.vector,
            step_function: NorthwestQuadrantNodeStepper = NorthwestQuadrantNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: NorthwestQuadrantNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> NorthwestQuadrantNodeStepper:
        return cast(NorthwestQuadrantNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NorthwestQuadrantSequenceRequest):
            return self.id == other.id
        return False