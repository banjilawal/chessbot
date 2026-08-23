# src/domain/exchange/request/crud/delete/id/chain/request.py

"""
Module: domain.exchange.request.crud.delete.id.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from domain import DeleteByIdRequest, Node

T = TypeVar("T", bound="Node")


class RemoveNodeByOffsetRequest(DeleteByIdRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         request_id: int
         item_id: int
         collection: Chain[T]

     Provides:
     
     Super Class:
        DeleteByIdRequest
     """
    
    def __init__(self, request_id: int, item_id: int, chain: Chain[T]):
        """
        Args:
            request_id: int
            item_id: int
            chain: Chain[T]
        """
        super().__init__(id=request_id, item_id=item_id, collection=chain)
        
    @property
    def chain(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
    
    @property
    def collection(self) -> Chain[T]:
        return self.chain
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, RemoveNodeByOffsetRequest):
            request = cast(RemoveNodeByOffsetRequest, other)
            return self.id == request.id
        return False