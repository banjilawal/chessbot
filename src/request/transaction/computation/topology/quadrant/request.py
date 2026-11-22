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

from domain import Vector
from request import TopologyRequest
from surface import Quadrant

T = TypeVar("T", bound="Quadrant")

class QuadrantTopologyRequest(TopologyRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        vector: Vector
        x_step: int
        slope: int

     Provides:

     Super Class:
        TopologyRequest
     """
    _x_step: int
    _slope: int
    
    def __init__(self, id: int, vector: Vector, x_step: int, slope: int):
        """
        Args:
            id: int
            vector: Vector
            x_step: int
            slope: int
        """
        super().__init__(id, vector=vector)
        self._x_step = x_step
        self._slope = slope
        
    @property
    def vector(self) -> Vector:
        return self._vector
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QuadrantTopologyRequest):
            return self.id == other.id
        return False