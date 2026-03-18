# src/logic/system/database/database.py

"""
Module: logic.system.database.database
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, TypeVar

from logic.system import (
    Context, DeletionResult, InsertionResult, IntegrityService, LoggingLevelRouter, SearchResult, Service
)

T = TypeVar("T")

class Database(Service, Generic[T]):
    """
    Role:
        -   Repo interface.
        -   Data Protection layer.

    Responsibilities:
        1.  Prevents direct access to data managed by StackService.
        2.  Middle layer between clients and StackService.

    Attributes:
        id: int
        name: str

    Provides:
        -   size() -> int
        -   is_empty() -> bool
        -   integrity_service() -> IntegrityService[T]
        -   iterator(self) -> iter
        -   insert(item: T) -> InsertionResult
        -   delete_by_id(id: int) -> DeletionResult[T]
        -   search(self, context: Context[T]) -> SearchResult[List[T]]

    Super:
        Service
    """
    
    def __init__(self, id: int, name: str):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name)
    
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
    def integrity_service(self) -> IntegrityService[T]:
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
        