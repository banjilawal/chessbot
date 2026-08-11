# src/authorization/request/operation/collection/deletion/chain.request.py

"""
Module: authorization.request.operation.collection.deletion.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from authorization import CollectionDeletionRequest
from collection import Chain

T = TypeVar("T", bound="Node")


class AddNodeRequest(CollectionDeletionRequest[Chain], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the ChainPop lifecycle.

     Attributes:
        node: T
        chain: Chain[T]

     Provides:
     
     Super Class:
        DeletionRequest
     """
    _node: T
    
    def __init__(self, id: int, node: T, chain: Chain[T]):
        """
        Args:
            id: int
            node: T
            chain: Chain[T]
        """
        super().__init__(id=id, collection=chain)
        self._node = node
    
    @property
    def node(self) -> T:
        return self._node
    
    @property
    def chain(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddNodeRequest):
            request = cast(AddNodeRequest, other)
            return self.id == request.id
        return False