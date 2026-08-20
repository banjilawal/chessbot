# src/request/insertion/chain/request.py

"""
Module: request.insertion.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from node import Node
from operation import AddNode
from request import InsertionRequest

T = TypeVar("T", bound="Node")


class AddNodeRequest(InsertionRequest[AddNode], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the AddNode lifecycle.

     Attributes:
         id: int
         item: T
         chain: Chain[T]

     Provides:
     
     Super Class:
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
    def collection(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddNodeRequest):
            request = cast(AddNodeRequest, other)
            return self._id == request.id
        return False