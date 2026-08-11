# src/request/operation/computation/request.py

"""
Module: request.operation.computation.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import OperationRequest
from result import ComputationResult


T = TypeVar("T", bound="ComputationOperation")


class ComputationRequest(OperationRequest[ComputationResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information through a ComputationOperation lifecycle.

     Attributes:

     Provides:
     
     Super Class:
        OperationRequest
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
        if isinstance(other, ComputationRequest):
            request = cast(ComputationRequest, other)
            return self.id == request.id
        return False