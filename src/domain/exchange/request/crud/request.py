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
from domain import Request

from artifcat.result import CrudResult

C = TypeVar("C", bound="DomainObjectCollection")
R = TypeVar("R", bound="CrudResult")


class CrudRequest(Request[R], ABC, Generic[C, R]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Transport the collection and other objects a CrudOperation needs to run a job.

     Attributes:
         id: int
         collection: C

     Provides:
     
     Super Class:
        Request
     """
    _collection: C
    
    def __init__(self, id: int, collection: C):
        """
        Args:
            id: int
            collection: C
        """
        super().__init__(id)
        self._collection = collection
        
    @property
    def collection(self) -> C:
        return self._collection
        
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, CrudRequest):
            request = cast(CrudRequest, other)
            return self.id == request.id
        return False