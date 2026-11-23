# src/request/transaction/computation/sequence/axis/east/request.py

"""
Module: request.transaction.computation.sequence.axis.east.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import AxisDelta, AxisDestination, Vector, VectorNode
from operation import EastAxisNodeStepper
from request import AxisSequenceRequest
from surface import EastAxis


class EastAxisSequenceRequest(AxisSequenceRequest[EastAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        delta: Vector
        terminus: Vector
        
     Provides:

     Super Class:
        AxisVectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = AxisDestination.EAST.vector,
            step_function: EastAxisNodeStepper = EastAxisNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: EastAxisNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> EastAxisNodeStepper:
        return cast(EastAxisNodeStepper, super().step_function)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EastAxisSequenceRequest):
            return self.id == other.id
        return False