# src/request/transaction/computation/sequence/axis/north/request.py

"""
Module: request.transaction.computation.sequence.axis.north.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import AxisDestination, Vector, VectorNode
from operation import NorthAxisNodeStepper
from request import AxisSequenceRequest
from surface import NorthAxis


class NorthAxisSequenceRequest(AxisSequenceRequest[NorthAxis]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: NorthAxisNodeStepper
        
     Provides:

     Super Class:
        AxisVectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector = AxisDestination.NORTH.vector,
            step_function: NorthAxisNodeStepper = NorthAxisNodeStepper()
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: NorthAxisNodeStepper
        """
        super().__init__(id=id, node=node, terminus=terminus, step_function=step_function)
    
    @property
    def step_function(self) -> NorthAxisNodeStepper:
        return cast(NorthAxisNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NorthAxisSequenceRequest):
            return self.id == other.id
        return False