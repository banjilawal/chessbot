# src/exchange/permissionRequest/permission/crud/delete/id/chain/request.py

"""
Module: exchange.request.permission.crud.delete.id.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from exchange import DeleteByIdPermissionRequest, Node

T = TypeVar("T", bound="Node")


class RemoveNodeByOffsetPermissionRequest(DeleteByIdPermissionRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1.  Transport information during the CrudOperation lifecycle.

     Attributes:
         permissionRequest_id: int
         item_id: int
         collection: Chain[T]

     Provides:
     
     Super Class:
        DeleteByIdPermissionRequest
     """
    
    def __init__(self, permissionRequest_id: int, item_id: int, chain: Chain[T]):
        """
        Args:
            permissionRequest_id: int
            item_id: int
            chain: Chain[T]
        """
        super().__init__(id=permissionRequest_id, item_id=item_id, collection=chain)
        
    @property
    def chain(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
    
    @property
    def collection(self) -> Chain[T]:
        return self.chain
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RemoveNodeByOffsetPermissionRequest):
            permissionRequest = cast(RemoveNodeByOffsetPermissionRequest, other)
            return self.id == permissionRequest.id
        return False