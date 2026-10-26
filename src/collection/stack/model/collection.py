# src/collection/stack/model/collection.py

"""
Module: collection.stack.model.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from collection import Stack
from domain import Model

T = TypeVar("T", bound="Model")


class ModelStack(Stack, ABC, Generic[T]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Stack of unique Model objects.

    Attributes:
        items: List[T]
 
    Provides:
    
    Super Class:
        Stack
    """
    
    def __init__(self, items: Optional[List[T]] | None = None):
        self._items = items or []
        super().__init__()
    
    @property
    def items(self) -> List[T]:
        return self._items
    
    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    @abstractmethod
    def push(self) -> InsertionResult:
        pass
    
    @property
    @abstractmethod
    def search(self) -> SearchResult[List[T]]:
        pass
    
    @property
    @abstractmethod
    def pop(self) -> DeletionResult[T]:
        pass
    
    @property
    @abstractmethod
    def iterator(self) -> Iterator[T]:
        pass