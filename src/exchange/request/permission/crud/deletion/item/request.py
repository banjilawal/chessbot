# src/exchange/permissionRequest/permission/crud/delete/item/request.py

"""
Module: exchange.request.permission.crud.delete.item.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import ExchangeObjectCollection
from exchange import DeletePermissionRequest, ExchangeDataObject

C = TypeVar("C", bound="ExchangeObjectCollection")
T = TypeVar("T", bound="ExchangeDataObject")


class DeleteItemPermissionRequest(DeletePermissionRequest, ABC, Generic[C, T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1.  Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item: T
         collection: C

     Provides:
     
     Super Class:
        DeletePermissionRequest
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
        if isinstance(other, DeleteItemPermissionRequest):
            permissionRequest = cast(DeleteItemPermissionRequest, other)
            return self.id == permissionRequest.id
        return False