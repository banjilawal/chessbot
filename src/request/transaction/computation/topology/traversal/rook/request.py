# src/request/transaction/computation/topology/traversal/rook/request.py

"""
Module: request.transaction.computation.topology.traversal.rook.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from domain import Rook, VectorNode
from request import (
    EastAxisSequenceRequest, NorthAxisSequenceRequest, SouthAxisSequenceRequest, TraversalTopologyRequest,
    WestAxisSequenceRequest
)
from util import IdFactory


class RookTopologyRequest(TraversalTopologyRequest[Rook]):
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
        TraversalTopologyRequest
     """
    
    def __init__(self, id: int, origin: VectorNode):
        """
        Args:
            id: int
            origin: VectorNode
        """
        super().__init__(id=id, origin=origin)
    
    @property
    def east_request(self) -> EastAxisSequenceRequest:
        return EastAxisSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def north_request(self) -> NorthAxisSequenceRequest:
        return NorthAxisSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def south_request(self) -> SouthAxisSequenceRequest:
        return SouthAxisSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def west_request(self) -> WestAxisSequenceRequest:
        return WestAxisSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def sequence_requests(self) -> List:
        return [
            self.east_request,
            self.north_request,
            self.south_request,
            self.west_request,
        ]
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RookTopologyRequest):
            return self.id == other.id
        return False