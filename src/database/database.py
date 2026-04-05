# src/database/database.py

"""
Module: database.database
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from result import DeletionResult, InsertionResult
from system import LoggingLevelRouter

T = TypeVar("T")


class Database(ABC, Generic[T]):
    """
    Role:
        _   Frontend
        -   Interface
        -   Data Protection

    Responsibilities:
        1.  Encapsulates StackService.
        2.  Protects data from direct access.

    Attributes:
        id: int
        size: int
        name: str
        iterator: iter
        is_empty: bool
        current_item: Optional[T]
        integrity_service: IntegrityMicroservice[T]

    Provides:
        -   iterator() ->: iter
        -   insert(item: T) -> InsertionResult:
        -   delete_by_id(id: int) -> DeletionResult[T]:
        -   search(context: Context[T]) -> SearchResult[List[T]]

    Super:
    """
    _id: id
    _name: str
    
    def __init__(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str
        """
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
    def size(self) -> int:
    
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        """Implement to test if the database is empty."""
        pass
    
    @property
    @abstractmethod
    def integrity_service(self) -> IntegrityMicroservice[T]:
        """"Implement to access the database's integrity service."""
        pass
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        """"Implement to access the database's integrity service."""
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
        