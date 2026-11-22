# src/request/transaction/computation/mapping/request.py

"""
Module: request.transaction.computation.mapping.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Vector
from request import ComputationRequest

T = TypeVar("T")

class MappingRequest(ComputationRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
         id: int
         vector: Vector

     Provides:

     Super Class:
        ComputationRequest
     """
    _vector: Vector
    
    def __init__(self, id: int, vector: Vector):
        """
        Args:
            id: int
        """
        super().__init__(id)
        self._vector = vector
        
        
    @property
    def vector(self) -> Vector:
        return self._vector
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ComputationRequest):
            return self.id == other.id
        return False