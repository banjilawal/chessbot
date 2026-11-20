# src/exchange/request/transaction/computation/product/request.py

"""
Module: exchange.request.transaction.computation.product.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Scalar, Vector
from exchange import ComputationRequest

class ScalarProductRequest(ComputationRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide product job details.

     Attributes:
        vector: Vector
        scalar: Scalar

     Provides:

     Super Class:
        ComputationRequest
     """
    
    _vector: Vector
    _scalar: Scalar

    def __init__(
            self,
            id: int,
            vector: Vector,
            scalar: Scalar,
    ):
        """
        Args:
            id: int
            vector: Vector
            scalar: Scalar
        """
        super().__init__(id)
        self._vector = vector
        self._scalar = scalar

    @property
    def vector(self) -> Vector:
        return  self._vector

    @property
    def scalar(self) -> Scalar:
        return self._scalar
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ScalarProductRequest):
            return self.id == other.id
        return False