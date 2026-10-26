# src/collection/stack/collection.py

"""
Module: collection.stack.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterator, List, Optional, TypeVar

from artifcat import DeletionResult, InsertionResult, SearchResult
from collection import DataStruct

T = TypeVar("T")


class Stack(DataStruct, ABC, Generic[T]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Interface for defining reliable stack of unique items.

    Attributes:
        size: int
        is_empty: bool
        is_not_empty: bool
        iterator: Iterator[T]

    Provides:

    Super Class:
    """
    
    _items: List[T]
    
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
    
    
