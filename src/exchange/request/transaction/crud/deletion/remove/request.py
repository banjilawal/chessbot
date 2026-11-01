# src/exchange/request/transaction/crud/deletion/remove/request.py

"""
Module: exchange.request.transaction.crud.deletion.remove.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from artifcat import DeletionResult
from repo.collection import Chain
from domain import Node
from exchange import DeletionRequest

R = TypeVar("R", bound="DeletionResult")
T = TypeVar("T", bound="Node")

class RemoveNodeRequest(DeletionRequest[R, T], ABC, Generic[R, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to a NodeRemoveer

     Attributes:
         id: int
         item: T
         collection: Chain[T]

     Provides:

     Super Class:
        DeletionRequest
     """
    
    def __init__(self, id: int, item: T, collection: Chain[T]):
        """
        Args:
            id: int
            item: T
            collection: Chain[T]
        """
        super().__init__(id, item=item, collection=collection)
        
    @property
    def item(self) -> T:
        return cast(T, super().item)
    
    @property
    def collection(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RemoveNodeRequest):
            return self.id == other.id
        return False