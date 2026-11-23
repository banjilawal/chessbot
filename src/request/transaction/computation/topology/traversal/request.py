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
from domain import TraversalRank, Vector, VectorNode
from request import TopologyRequest

T = TypeVar("T", bound="TraversalRank")

class TraversalTopologyRequest(TopologyRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide a ComputationWorker details about a job.

     Attributes:
        id: int
        origin: VectorNode

     Provides:

     Super Class:
        TopologyRequest
     """
    
    def __init__(self, id: int, origin: VectorNode):
        """
        Args:
            id: int
            origin: VectorNode
        """
        super().__init__(id, origin=origin)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TraversalTopologyRequest):
            return self.id == other.id
        return False