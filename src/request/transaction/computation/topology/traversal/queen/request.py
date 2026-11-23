# src/request/transaction/computation/topology/traversal/queen/request.py

"""
Module: request.transaction.computation.topology.traversal.queen.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List

from domain import Queen, VectorNode
from request import (
    EastAxisSequenceRequest, NorthAxisSequenceRequest, NortheastQuadrantSequenceRequest,
    NorthwestQuadrantSequenceRequest, SouthAxisSequenceRequest, SoutheastQuadrantSequenceRequest,
    SouthwestQuadrantSequenceRequest, TraversalTopologyRequest, WestAxisSequenceRequest
)
from util import IdFactory


class QueenTraversalTopologyRequest(TraversalTopologyRequest[Queen]):
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
    def northeast_request(self) -> NortheastQuadrantSequenceRequest:
        return NortheastQuadrantSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def northwest_request(self) -> NorthwestQuadrantSequenceRequest:
        return NorthwestQuadrantSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def southeast_request(self) -> SoutheastQuadrantSequenceRequest:
        return SoutheastQuadrantSequenceRequest(
            node=self.origin,
            id=IdFactory.next_id(class_name="Request"),
        )
    
    @property
    def southwest_request(self) -> SouthwestQuadrantSequenceRequest:
        return SouthwestQuadrantSequenceRequest(
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
            self.northeast_request,
            self.northwest_request,
            self.southeast_request,
            self.southwest_request,
        ]
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, QueenTraversalTopologyRequest):
            return self.id == other.id
        return False