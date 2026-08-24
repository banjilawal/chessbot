# src/domain/exchange/request/crud/delete/request.py

"""
Module: domain.exchange.request.crud.delete.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from collection import DomainObjectCollection
from domain import CrudRequest, DomainObject
from artifcat import DeletionResult


T = TypeVar("T", bound="DomainObject")


class DeleteRequest(CrudRequest[DeletionResult], ABC, Generic[T]):
    """
     Role:
         -  Messaging
         -  Transport

     Responsibilities:
        1. Provide a collection and details about the item a Deleter needs to run a job.

     Attributes:
         id: int
         collection: DomainObjectCollection[T]

     Provides:
     
     Super Class:
        CrudRequest
     """
    
    def __init__(self, id: int, collection: DomainObjectCollection[T]):
        """
        Args:
            id: int
            collection: DomainObjectCollection[T]
        """
        super().__init__(id, collection=collection)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, DeleteRequest):
            request = cast(DeleteRequest, other)
            return self.id == request.id
        return False