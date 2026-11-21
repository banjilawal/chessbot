# src/request/transaction/computation/distance/request.py

"""
Module: request.transaction.computation.distance.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Vector
from request import DistanceRequest


class EuclideanDistanceRequest(DistanceRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide distance job details.

     Attributes:
        u: Vector
        v: Vector

     Provides:

     Super Class:
        ComputationRequest
     """
    
    _u: Vector
    _v: Vector

    def __init__(self, id: int, u: Vector, v: Vector):
        """
        Args:
            id: int
            u: Vector
            v: Vector
        """
        super().__init__(id, u=u, v=v)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EuclideanDistanceRequest):
            return self.id == other.id
        return False