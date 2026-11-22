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
from request import MappingRequest
from surface import Axis

T = TypeVar("T", bound="Axis")

class AxisMappingRequest(MappingRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        vector: Vector
        delta: Vector

     Provides:

     Super Class:
        MappingRequest
     """

    _delta: Vector
    
    def __init__(self, id: int, vector: Vector, delta: Vector):
        """
        Args:
            id: int
            vector: Vector
            delta: Vector
        """
        super().__init__(id, vector=vector)
        self._delta = delta
    
    @property
    def delta(self) -> Vector:
        return self._delta
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AxisMappingRequest):
            return self.id == other.id
        return False