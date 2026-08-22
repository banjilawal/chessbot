# src/domain/exchange/request/crud/delete/item/request.py

"""
Module: domain.exchange.request.crud.delete.item.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import DeleteRequest, DomainObject

C = TypeVar("C", bound="DomainObjectCollection")
T = TypeVar("T", bound="DomainObject")


class DeleteItemRequest(DeleteRequest, ABC, Generic[C, T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item: T
         collection: C

     Provides:
     
     Super Class:
        DeleteRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, collection: C):
        """
        Args:
            id: int
            item: T
            collection: C
        """
        super().__init__(id=id, collection=collection)
        self._item = item
        
    @property
    def item(self) -> T:
        return self._item
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeleteItemRequest):
            request = cast(DeleteItemRequest, other)
            return self.id == request.id
        return False