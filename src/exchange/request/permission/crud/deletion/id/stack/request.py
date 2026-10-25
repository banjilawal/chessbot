# src/exchange/permissionRequest/permission/crud/delete/id/stack/request.py

"""
Module: exchange.request.permission.crud.delete.id.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import StackService
from exchange import DeleteByIdPermissionRequest, StateModel


T = TypeVar("T", bound="StateModel")


class PopStackByIdPermissionRequest(DeleteByIdPermissionRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1.  Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item_id: int
         collection: StackService[T]

     Provides:
     
     Super Class:
        DeleteByIdPermissionRequest
     """
    
    def __init__(self, permissionRequest_id: int, item_id: int, stack: StackService[T]):
        """
        Args:
            permissionRequest_id: int
            item_id: int
            stack: StackService[T]
        """
        super().__init__(id=permissionRequest_id, item_id=item_id, collection=stack)
        
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    @property
    def collection(self) -> StackService[T]:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PopStackByIdPermissionRequest):
            permissionRequest = cast(PopStackByIdPermissionRequest, other)
            return self.id == permissionRequest.id
        return False