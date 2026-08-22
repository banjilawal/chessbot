# src/domain/exchange/request/operation/computation.vector/product/request.py

"""
Module: domain.exchange.request.operation.computation.vector.product.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import cast

from authorization import VectorComputationRequest


class VectorProductRequest(VectorComputationRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information to execute an operation

     Attributes:

     Provides:
     
     Super Class:
        VectorComputationRequest
     """
    _id: int
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        super().__init__(id=id)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorProductRequest):
            request = cast(VectorProductRequest, other)
            return self.id == domain.exchange.request.id
        return False