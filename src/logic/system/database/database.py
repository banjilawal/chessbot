# src/logic/system/database/service.py

"""
Module: logic.system.database.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, Optional, TypeVar

from logic import Context, ContextService, IntegrityService, SearchResult
from logic.system import Service, InsertionResult, LoggingLevelRouter


T = TypeVar("T")

class Database(Service, Generic[T]):
    """
    # ROLE: Unique Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Assures StackService only stores unique data with no duplicates.
    2.  Interface for inserting data into the StackService.
    3.  Protects data from direct access.
    4.  Wrapper for StackService
    5.  Public facing API.
    
    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
        
    # INHERITED ATTRIBUTES:
    None
    """
    def __init__(self, id: int, name: str):
        super().__init__(id=id, name=name)
    
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
        
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @abstractmethod
    def integrity_service(self) -> IntegrityService[T]:
        pass
        
    @abstractmethod
    def context_service(self) -> ContextService[T]:
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def insert(self, item: T) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(self, id: int) -> InsertionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def search(self, context: Context[T]) -> SearchResult[List[T]]:
        pass
        