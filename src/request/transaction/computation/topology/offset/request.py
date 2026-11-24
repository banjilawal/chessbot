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

from collection import VectorSet
from domain import OffsetRank, VectorNode
from request import TopologyRequest

T = TypeVar("T", bound="OffsetRank")

class OffsetTopologyRequest(TopologyRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: VectorNode
        offsets: VectorSet

     Provides:

     Super Class:
        TopologyRequest
     """

    _offsets: VectorSet
    
    def __init__(self, id: int, origin: VectorNode, offsets: VectorSet):
        """
        Args:
            id: int
            origin: VectorNode
            offsets: VectorSet
        """
        super().__init__(id=id, origin=origin)
        self._offsets = offsets
    
    @property
    def offsets(self) -> VectorSet:
        return self._offsets
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, OffsetTopologyRequest):
            return self.id == other.id
        return False