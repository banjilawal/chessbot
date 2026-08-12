# src/request/operation/collection/insertion/chain.request.py

"""
Module: request.operation.collection.insertion.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast


from collection import Chain
from request import InsertionRequest

T = TypeVar("T", bound="Node")


class AddNodeRequest(InsertionRequest[Chain], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Transport job information throughout the AddChainNode lifecycle.

     Attributes:
        item: T
        chain: Chain[T]

     Provides:
     
     Super Class:
        InsertionRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, chain: Chain[T]):
        """
        Args:
            id: int
            item: T
            chain: Chain[T]
        """
        super().__init__(id=id, collection=chain)
        self._item = item
    
    @property
    def item(self) -> T:
        return self._item
    
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