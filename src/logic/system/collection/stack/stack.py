# src/logic/system/collection/stack/exception/stack.py

"""
Module: logic.system.collection.stack.exception.stack
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, Optional, TypeVar

from logic.system import (
    Context, IdentityService, InsertionResult, LoggingLevelRouter, IntegrityMicroservice, DeletionResult,
    SearchResult
)

T = TypeVar("T")
C = TypeVar("C", bound=Context)

class StackService(ABC, Generic[T]):
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
        stack: str

    Provides:
        -   id: int
        -   stack: str
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
        -   query(collider_candidates: List[T], query: Context[T]) -> SearchResult[List[T]]

    Super class:
    """
    _id: int
    _name: str

    def __init__(self, id: int, name: str,):
        self._id = id
        self._name = name
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    @abstractmethod
    def items(self) -> List[T]:
        """Implement to access the stack's items"""
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> Iterator[T]:
        """Implement to access the stack's iterator."""
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        """Implement to return the size of the stack."""
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """Implement to test if the stack is empty."""
        pass
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        """Implement to get the item ontop of the stack."""
        pass

    @property
    @abstractmethod
    def integrity_service(self) -> IntegrityMicroservice[T]:
        """"Implement to access the model's integrity service."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: T) -> InsertionResult:
        """Implement to push a new item into the stack."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[T]:
        """Implement to pop an item from the stack."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()) -> DeletionResult[T]:
        """Implement to delete an item from the stack."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def query(self, context: Context[T]) -> SearchResult[List[T]]:
        """Implement to read from the stack.'"""
        pass