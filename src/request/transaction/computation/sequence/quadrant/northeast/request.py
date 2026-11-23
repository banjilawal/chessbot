# src/request/transaction/computation/sequence/quadrant/northeast/request.py

"""
Module: request.transaction.computation.sequence.quadrant.northeast.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import QuadrantDestination, Vector, VectorNode
from operation import NortheastQuadrantNodeStepper
from request import QuadrantSequenceRequest
from surface import NortheastQuadrant


class NortheastQuadrantSequenceRequest(QuadrantSequenceRequest[NortheastQuadrant]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: NortheastQuadrantNodeStepper

     Provides:

     Super Class:
        QuadrantSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = QuadrantDestination.NORTHEAST.vector,
            step_function: NortheastQuadrantNodeStepper = NortheastQuadrantNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: NortheastQuadrantNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> NortheastQuadrantNodeStepper:
        return cast(NortheastQuadrantNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NortheastQuadrantSequenceRequest):
            return self.id == other.id
        return False