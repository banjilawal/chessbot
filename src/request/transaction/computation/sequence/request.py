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

     Provides:

     Super Class:
        ComputationRequest
     """
    _origin: VectorNode
    _terminus: Vector
    
    def __init__(self, id: int, origin: VectorNode, terminus: Vector):
        """
        Args:
            id: int
            origin: VectorNode
            terminus: Vector
        """
        super().__init__(id)
        self._origin = origin
        self._terminus = terminus
        
    @property
    def origin(self) -> VectorNode:
        return self._origin
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeSequenceRequest):
            return self.id == other.id
        return False