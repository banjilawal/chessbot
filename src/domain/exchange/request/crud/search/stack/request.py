# src/domain/exchange/request/crud/search/stack/request.py

"""
Module: domain.exchange.request.crud.search.stack.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""
from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import StackService
from domain import SearchContext, SearchRequest, StateDataModelObject

T = TypeVar("T", bound="StateDataModelObject")

class StackSearchRequest(SearchRequest, ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a collection and criteria a Searcher needs to run a job.

     Attributes:
         id: int
         context: SearchContext[T]
         collection: StackService[T]

     Provides:
     
     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: SearchContext[T], stack: StackService[T]):
        """
        Args:
            id: int
            context: SearchContext[T]
            stack: StackService[T]
        """
        super().__init__(id=id, context=context, collection=stack)
        
    @property
    def context(self) -> SearchContext[T]:
        return cast(SearchContext[T], super().context)
        
    @property
    def stack(self) -> StackService[T]:
        return cast(StackService[T], super().collection)
    
    @property
    def collection(self) -> StackService[T]:
        return self.stack
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, StackSearchRequest):
            request = cast(StackSearchRequest, other)
            return self.id == request.id
        return False