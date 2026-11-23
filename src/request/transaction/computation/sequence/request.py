# src/request/transaction/computation/topology/request.py

"""
Module: request.transaction.computation.topology.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Vector, VectorNode
from operation import SpaceNodeStepper
from request import ComputationRequest
from surface import Space

T = TypeVar("T", bound="Space")

class VectorNodeSequenceRequest(ComputationRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
         id: int
         origin: VectorNode
         step_function: SpaceNodeStepper[T]

     Provides:

     Super Class:
        ComputationRequest
     """
    _origin: VectorNode
    _terminus: Vector
    _step_function: SpaceNodeStepper[T]
    
    def __init__(
            self,
            id: int,
            origin: VectorNode,
            terminus: Vector,
            step_function: SpaceNodeStepper[T],
    ):
        """
        Args:
            id: int
            origin: VectorNode
            terminus: Vector
            step_function: SpaceNodeStepper[T]
        """
        super().__init__(id)
        self._origin = origin
        self._terminus = terminus
        self._step_function = step_function
        
    @property
    def origin(self) -> VectorNode:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    @property
    def step_function(self) -> SpaceNodeStepper:
        return self._step_function
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeSequenceRequest):
            return self.id == other.id
        return False