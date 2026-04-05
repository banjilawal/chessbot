# src/logic/system/collection/schema/exception/schema.py

"""
Module: logic.system.collection.schema.exception.schema
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, Optional, TypeVar

from system import (
    Context, IdentityService, InsertionResult, LoggingLevelRouter, IntegrityMicroservice, DeletionResult,
    Microservice, SearchResult
)

T = TypeVar("T")

class StackService(Microservice[T], Generic[T]):
    """
    Role:
        -   Data layer
        -   CRUD controller.
        -   ACID compliance.
        -   Microservice API
        -   Interface

    Responsibilities:
        1.  Preserve consistency during updates and deletes.
        2.  Stateful, scalable integrity management of objects.
        3.  Grant read access to the data-modeling objects.

    Attributes:
        id: int
        schema: str

    Provides:
        -   id: int
        -   schema: str
        -   items() -> List[T]
        -   size() -> int
        -   iterator() -> Iterator[T]
        -   is_empty() -> bool
        -   current_item(self) -> T
        -   integrity_service() -> IntegrityMicroservice[T]
        -   context_service(self) -> QueryService[T]
        -   push(item: T) -> InsertionResult
        -   pop() -> DeletionResult[T]
        -   delete_by_id(id: int) -> DeletionResult[T]
        -   context(collider_candidates: List[T], context: Context[T]) -> SearchResult[List[T]]

    Super class:
    """
    _id: int
    _name: str

    def __init__(self, id: int, name: str,):
        super().__init__(id=id, name=name)
    
    @property
    @abstractmethod
    def items(self) -> List[T]:
        """Implement to access the schema's items"""
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> Iterator[T]:
        """Implement to access the schema's iterator."""
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        """Implement to return the size of the schema."""
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """Implement to test if the schema is empty."""
        pass
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        """Implement to get the item ontop of the schema."""
        pass

    @property
    @abstractmethod
    def integrity_service(self) -> IntegrityMicroservice[T]:
        """"Implement to access the model's integrity service."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: T) -> InsertionResult:
        """Implement to push a new item into the schema."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[T]:
        """Implement to pop an item from the schema."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()) -> DeletionResult[T]:
        """Implement to delete an item from the schema."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, context: Context[T]) -> SearchResult[List[T]]:
        """Implement to read from the schema.'"""
        pass