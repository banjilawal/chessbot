# src/request/transaction/crud/insertion/add/request.py

"""
Module: request.transaction.crud.insertion.add.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar


from collection import Chain
from domain import Node
from request import InsertionRequest

T = TypeVar("T", bound="Node")

class AddNodeRequest(InsertionRequest[T], ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a NodeAdder

     Attributes:
         id: int
         item: T
         collection: Chain[T]
         offset: int

     Provides:

     Super Class:
        InsertionRequest
     """
    _offset: int
    
    def __init__(
            self,
            id: int,
            item: T,
            collection: Chain[T],
            offset: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            item: T
            collection: Chain[T]
            offset: Optional[int]
        """
        super().__init__(id=id, item=item, collection=collection)
        self._offset = offset or 0
        
    @property
    def offset(self) -> int:
        return self._offset
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddNodeRequest):
            return self.id == other.id
        return False