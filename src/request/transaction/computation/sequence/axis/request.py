# src/request/transaction/computation/sequence/request.py

"""
Module: request.transaction.computation.sequence.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import Vector, VectorNode
from operation import AxisNodeStepper
from request import VectorNodeSequenceRequest
from surface import Axis

T = TypeVar("T", bound="Axis")

class AxisSequenceRequest(VectorNodeSequenceRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: AxisNodeStepper

     Provides:

     Super Class:
        VectorNodeSequenceRequest
     """

    _delta: Vector
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector,
            step_function: AxisNodeStepper,
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: AxisNodeStepper
        """
        super().__init__(
            id,
            node=node,
            terminus=terminus,
            step_function=step_function
        )
    
    @property
    def step_function(self) -> AxisNodeStepper:
        return cast(AxisNodeStepper, super().step_function)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AxisSequenceRequest):
            return self.id == other.id
        return False