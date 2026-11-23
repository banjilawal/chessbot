# src/request/transaction/computation/sequence/axis/south/request.py

"""
Module: request.transaction.computation.sequence.axis.south.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import AxisDelta, AxisDestination, Vector, VectorNode
from operation import SouthAxisNodeStepper
from request import AxisSequenceRequest
from surface import SouthAxis


class SouthAxisSequenceRequest(AxisSequenceRequest[SouthAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: SouthAxisNodeStepper
        
     Provides:

     Super Class:
        AxisVectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = AxisDestination.SOUTH.vector,
            step_function: SouthAxisNodeStepper = SouthAxisNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: SouthAxisNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) ->SouthAxisNodeStepper:
        return cast(SouthAxisNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, SouthAxisSequenceRequest):
            return self.id == other.id
        return False