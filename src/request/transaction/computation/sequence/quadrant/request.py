# src/request/transaction/computation/sequence/request.py

"""
Module: request.transaction.computation.sequence.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

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
        x_step: int
        slope: int

     Provides:

     Super Class:
        VectorNodeSequenceRequest
     """
    _x_step: int
    _slope: int
    
    def __init__(
            self,
            id: int,
            node: VectorNode,
            x_step: int,
            slope: int,
            terminus: Vector,
            step_function: Optional[QuadrantNodeStepper] | None = None,
    ):
        """
        Args:
            id: int
            node: VectorNode
            x_step: int
            slope: int
            terminus: Vector
            step_function: Optional[QuadrantNodeStepper]
        """
        super().__init__(
            id,
            node=node,
            terminus=terminus,
            step_function=step_function or QuadrantNodeStepper(),
        )
        self._x_step = x_step
        self._slope = slope
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QuadrantSequenceRequest):
            return self.id == other.id
        return False