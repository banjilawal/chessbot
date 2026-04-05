# src/database/__init__.py

"""
Module: database.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from result import DeletionResult, InsertionResult
from stack import StackService
from system import LoggingLevelRouter

T = TypeVar("T")


class Database(ABC, Generic[T]):
    """
    Role:
        -   Data Protection

    Responsibilities:
        1.  Protects StackService data from direct access.
        2.  Middle layer between clients and StackService.
        3.  Platform for extending StackService features.

    Attributes:
        id: int
        size: int
        name: str
        is_empty: bool
        integrity_service: IntegrityMicroservice[T]

    Provides:
        -   iterator() ->: iter
        -   insert(item: T) -> InsertionResult:
        -   delete_by_id(id: int) -> DeletionResult[T]:
        -   search(context: Context[T]) -> SearchResult[List[T]]

    Super:
    """
    
    def __init__(self,id: int,name: str,):
        """
        Args:
            id: int
            name: str
        """
        
    @property
    @abstractmethod
    def size(self) -> int:
        """Implement to return the size of the database."""
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """Implement to test if the database is empty."""
        pass
    
    @property
    @abstractmethod
    def integrity_service(self) -> IntegrityMicroservice[T]:
        """"Implement to access the model's integrity service."""
        pass
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        """"Implement to access the model's integrity service."""
        pass

    @property
    @abstractmethod
    def iterator(self) -> iter:
        """Implement to access the database's iterator."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def insert(self, item: T) -> InsertionResult:
        """Implement to insert a new item into the database."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(self, id: int) -> DeletionResult[T]:
        """Implement to delete an item from the database."""
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, context: Context[T]) -> SearchResult[List[T]]:
        """Implement to read from the database.'"""
        pass
        