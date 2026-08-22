# src/domain/exchange/request/crud/insert/request.py

"""
Module: domain.exchange.request.crud.insert.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import CrudRequest, DomainObject
from result import InsertionResult


T = TypeVar("T", bound="DomainObject")


class InsertRequest(CrudRequest[InsertionResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
         1. Transport information during the CrudOperation lifecycle.

     Attributes:
         id: int
         item: T
         collection: DomainObjectCollection[T]

     Provides:
     
     Super Class:
        CrudRequest
     """
    _item: T
    
    def __init__(self, id: int, item: T, collection: DomainObjectCollection[T]):
        """
        Args:
            id: int
            item: T
            collection: DomainObjectCollection[T]
        """
        super().__init__(id=id, collection=collection)
        self._item = item
    
    @property
    def item(self) -> T:
        return self._item
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, InsertRequest):
            request = cast(InsertRequest, other)
            return self.id == request.id
        return False