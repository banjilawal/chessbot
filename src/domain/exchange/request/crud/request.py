# src/domain/exchange/request/crud/request.py

"""
Module: domain.exchange.request.crud.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import DomainObject, Request
from result import CrudResult

T = TypeVar("T", bound="DomainObject")


class CrudRequest(Request[CrudResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         collection: DomainObjectCollection[T]

     Provides:
     
     Super Class:
        Request
     """
    _collection: DomainObjectCollection[T]
    
    def __init__(self, id: int, collection: DomainObjectCollection[T]):
        """
        Args:
            id: int
            collection: DomainObjectCollection[T]
        """
        super().__init__(id)
        self._collection = collection
        
    @property
    def collection(self) -> DomainObjectCollection[T]:
        return self._collection
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CrudRequest):
            request = cast(CrudRequest, other)
            return self.id == request.id
        return False