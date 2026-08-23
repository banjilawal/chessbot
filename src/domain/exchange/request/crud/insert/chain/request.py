# src/domain/exchange/request/crud/insert/chain/request.py

"""
Module: domain.exchange.request.crud.insert.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from domain import InsertRequest, Node

T = TypeVar("T", bound="Node")

class AddNodeRequest(InsertRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item: T
         collection: Chain[T]

     Provides:
     
     Super Class:
        InsertRequest
     """
    
    def __init__(self, id: int, item: T, chain: Chain[T]):
        """
        Args:
            id: int
            item: T
            chain: Chain[T]
        """
        super().__init__(id=id, item=item, collection=chain)
    
    @property
    def item(self) -> T:
        return cast(T, super().item)
        
    @property
    def chain(self) -> Chain[T]:
        return cast(Chain[T], super().collection)
    
    @property
    def collection(self) -> Chain[T]:
        return self.chain
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddNodeRequest):
            request = cast(AddNodeRequest, other)
            return self.id == request.id
        return False