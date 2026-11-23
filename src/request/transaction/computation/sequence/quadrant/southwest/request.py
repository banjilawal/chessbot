# src/request/transaction/computation/sequence/quadrant/southwest/request.py

"""
Module: request.transaction.computation.sequence.quadrant.southwest.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import QuadrantDestination, QuadrantStepFunction, Vector, VectorNode
from operation import SouthwestQuadrantNodeStepper
from request import QuadrantSequenceRequest
from surface import SouthwestQuadrant


class SouthwestQuadrantSequenceRequest(QuadrantSequenceRequest[SouthwestQuadrant]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: SouthwestQuadrantNodeStepper

     Provides:

     Super Class:
        QuadrantSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = QuadrantDestination.SOUTHWEST.vector,
            step_function: SouthwestQuadrantNodeStepper = SouthwestQuadrantNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: SouthwestQuadrantNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> SouthwestQuadrantNodeStepper:
        return cast(SouthwestQuadrantNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SouthwestQuadrantSequenceRequest):
            return self.id == other.id
        return False