# src/request/transaction/computation/sequence/request.py

"""
Module: request.transaction.computation.sequence.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Vector, VectorNode
from operation import QuadrantNodeStepper
from request import VectorNodeSequenceRequest
from surface import Quadrant

T = TypeVar("T", bound="Quadrant")

class QuadrantSequenceRequest(VectorNodeSequenceRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        node: VectorNode
        terminus: Vector
        step_function: QuadrantNodeStepper

     Provides:

     Super Class:
        VectorNodeSequenceRequest
     """
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            terminus: Vector,
            step_function: QuadrantNodeStepper,
    ):
        """
        Args:
            id: int
            node: VectorNode
            terminus: Vector
            step_function: QuadrantNodeStepper
        """
        super().__init__(
            id,
            node=node,
            terminus=terminus,
            step_function=step_function,
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QuadrantSequenceRequest):
            return self.id == other.id
        return False