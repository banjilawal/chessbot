# src/domain/exchange/request/crud/delete/id/request.py

"""
Module: domain.exchange.request.crud.delete.id.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import DeleteRequest

T = TypeVar("T", bound="DomainObjectCollection")



class DeleteByIdRequest(DeleteRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item_id: int
         collection: C

     Provides:
     
     Super Class:
        DeleteRequest
     """
    _item: T
    
    def __init__(self, request_id: int, item_id: int, collection: C):
        """
        Args:
            request_id: int
            item_id: int
            collection: C
        """
        super().__init__(id=request_id, collection=collection)
        self._item_id = item_id
        
    @property
    def item_id(self) -> int:
        return self._item_id
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeleteByIdRequest):
            request = cast(DeleteByIdRequest, other)
            return self.id == request.id
        return False