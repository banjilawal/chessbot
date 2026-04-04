# src/logic/system/database/database.py

"""
Module: logic.system.database.database
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, Optional, TypeVar

from system import (
    Context, DeletionResult, InsertionResult, IntegrityMicroservice, LoggingLevelRouter, SearchResult, Microservice
)

T = TypeVar("T")

class Database(Microservice, Generic[T]):
    """
    Role:
        -   Repo interface.
        -   Data Protection layer.

    Responsibilities:
        1.  Protects StackService data from direct access.
        2.  Middle layer between clients and StackService.
        3.  Platform for extending StackService features.

    Attributes:
        id: int
        schema: str

    Provides:
        -   size() -> int
        -   is_empty() -> bool
        -   integrity_service() -> IntegrityMicroservice[T]
        -   iterator(self) -> iter
        -   insert(item: T) -> InsertionResult
        -   delete_by_id(id: int) -> DeletionResult[T]
        -   search(self, context: Context[T]) -> SearchResult[List[T]]

    Super:
        Microservice
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
        