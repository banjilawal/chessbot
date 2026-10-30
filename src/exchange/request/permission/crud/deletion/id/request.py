# src/exchange/request/permission/crud/delete/id/request.py

"""
Module: exchange.request.permission.crud.delete.id.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import ExchangeObjectCollection
from exchange import DeletePermissionRequest

T = TypeVar("T", bound="ExchangeObjectCollection")



class DeleteByIdPermissionRequest(DeletePermissionRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1.  Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item_id: int
         collection: C

     Provides:
     
     Super Class:
        DeletePermissionRequest
     """
    _item: T
    
    def __init__(self, permissionRequest_id: int, item_id: int, collection: C):
        """
        Args:
            permissionRequest_id: int
            item_id: int
            collection: C
        """
        super().__init__(id=permissionRequest_id, collection=collection)
        self._item_id = item_id
        
    @property
    def item_id(self) -> int:
        return self._item_id
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeleteByIdPermissionRequest):
            permissionRequest = cast(DeleteByIdPermissionRequest, other)
            return self.id == permissionRequest.id
        return False