# src/request/operation/computation.vector/transform/request.py

"""
Module: request.operation.computation.vector.transform.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import cast

from authorization import VectorComputationRequest


class VectorTransformRequest(VectorComputationRequest):
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
        if isinstance(other, VectorTransformRequest):
            request = cast(VectorTransformRequest, other)
            return self.id == request.id
        return False