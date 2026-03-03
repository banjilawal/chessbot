# src/logic/system/collection/stack/exception/stack.py

"""
Module: logic.system.collection.stack.exception.stack
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from logic.system import (
    Context, ContextService, IdentityService, InsertionResult, LoggingLevelRouter, IntegrityService, DeletionResult,
    SearchResult
)

T = TypeVar("T")
C = TypeVar("C", bound=Context)

class StackService(ABC, Generic[T]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Scales Builder and Validator operations for collection of objects.
    2.  Provides map aware search.
    3.  Safe and reliable CRUD operations.
    4.  Public facing API.
    
    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int):
        *   name (str):
    
    # INHERITED ATTRIBUTES:
    None
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
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def current_item(self) -> Optional[T]:
        pass

    @property
    @abstractmethod
    def integrity_service(self) -> IntegrityService[T]:
        pass
    
    @property
    @abstractmethod
    def context_service(self) -> ContextService[C]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: T) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            self,
            id: int,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[T]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def query(self, dataset: List[T], context: C) -> SearchResult[List[T]]:
        pass