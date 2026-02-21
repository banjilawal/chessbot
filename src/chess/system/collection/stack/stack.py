# src/chess/system/collection/stack/exception/stack.py

"""
Module: chess.system.collection.stack.exception.stack
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system import (
    Context, ContextService, InsertionResult, LoggingLevelRouter, EntityService, DeletionResult, SearchResult
)

D = TypeVar("D")
C = TypeVar("C", bound=Context)

class StackService(ABC, Generic[D]):
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

    def stack(self, id: int, name: str,):
        self._id = id
        self._name = name
        #
        # self._size = len(self._items)
        # self._current_items = self._items[-1] if self._items else None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
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
    def current_item(self) -> Optional[D]:
        pass

    @property
    @abstractmethod
    def integrity_service(self) -> EntityService[D]:
        pass
    
    @property
    @abstractmethod
    def context_service(self) -> ContextService[C]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: D) -> InsertionResult:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def pop(self) -> DeletionResult[D]:
        pass
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def query(self, dataset: List[D], context: C) -> SearchResult[List[D]]:
        pass