# src/request/transaction/computation/sequence/axis/west/request.py

"""
Module: request.transaction.computation.sequence.axis.west.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import AxisDestination, Vector, VectorNode
from operation import WestAxisNodeStepper
from request import AxisSequenceRequest
from surface import WestAxis


class WestAxisSequenceRequest(AxisSequenceRequest[WestAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: WestAxisNodeStepper
        
     Provides:

     Super Class:
        AxisVectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = AxisDestination.WEST.vector,
            step_function: WestAxisNodeStepper = WestAxisNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: WestAxisNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> WestAxisNodeStepper:
        return cast(WestAxisNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, WestAxisSequenceRequest):
            return self.id == other.id
        return False