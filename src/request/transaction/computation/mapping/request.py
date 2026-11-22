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

from domain import VectorNode
from request import ComputationRequest
from surface import Space

T = TypeVar("T", bound="Space")

class MappingRequest(ComputationRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
         id: int
         node: VectorNode

     Provides:

     Super Class:
        ComputationRequest
     """
    _node: VectorNode
    
    def __init__(self, id: int, node: VectorNode):
        """
        Args:
            id: int
        """
        super().__init__(id)
        self._node = node
        
        
    @property
    def node(self) -> VectorNode:
        return self._node
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ComputationRequest):
            return self.id == other.id
        return False