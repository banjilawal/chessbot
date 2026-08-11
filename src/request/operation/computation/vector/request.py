# src/request/operation/computation/vector/request.py

"""
Module: request.operation.computation.vector.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import TypeVar, cast

from authorization import ComputationRequest, VectorComputationRequest


T = TypeVar("T", bound="Result")


class VectorComputationRequest(ComputationRequest):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information to execute an operation

     Attributes:

     Provides:
     
     Super Class:
        Request
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
        if isinstance(other, VectorComputationRequest):
            request = cast(VectorComputationRequest, other)
            return self.id == request.id
        return False