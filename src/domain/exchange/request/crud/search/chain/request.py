# src/domain/exchange/request/crud/search/chain/request.py

"""
Module: domain.exchange.request.crud.search.chain.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import Chain
from domain import SearchRequest, Node

T = TypeVar("T", bound="Node")

class AddNodeRequest(SearchRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         context: T
         collection: Chain[T]

     Provides:
     
     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: T, chain: Chain[T]):
        """
        Args:
            id: int
            context: T
            chain: Chain[T]
        """
        super().__init__(id=id, context=context, collection=chain)
    
    @property
    def context(self) -> T:
        return cast(T, super().context)
        
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