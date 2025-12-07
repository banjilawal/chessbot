# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system import (
    Context, DataServiceException, InsertionResult, LoggingLevelRouter, PoppingEmptyStackException, SearchResult,
    Finder, EntityService, DeletionResult
)


D = TypeVar("D")
C = TypeVar("C", binding=Context[D])

class DataService(ABC, Generic[D]):
    """
    # ROLE: Data Stack, Finder EntityService, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Scales Builder and Validator operations for collection of objects.
    2.  Provides context aware Finder.
    3.  Safe and reliable CRUD operations.
    4.  Public facing API.
    
    # PARENT
    None

    # PROVIDES:
        *   Builder
        *   Validator
        *   Finder
        *   Insertion
        *   Deletin

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   items (List[D]):
        *   searcher (Finder[D]):
        *   service (EntityService[D]):
        *   context_service (EntityService[C]);
        *   current_item (D):
        *   size (int):
    """
    _id: int
    _name: str
    _items: List[D]
    _service: EntityService[D]
    _context_service: EntityService[C]

    def __init__(
            self,
            id: int,
            name: str,
            items: List[D],
            service: EntityService[D],
            context_service: EntityService[C],
    ):
        self._id = id
        self._name = name
        self._items = items
        self._service = service
        self._context_service = context_service
        #
        # self._size = len(self._items)
        # self._current_item = self._items[-1] if self._items else None
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def size(self) -> int:
        return len(self._items)
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def items(self) -> List[D]:
        return self._items
    
    @property
    def service(self) -> EntityService[D]:
        return self._service
    
    @property
    def context_service(self) -> EntityService[C]:
        return self._context_service
    
    @property
    def current_item(self) -> Optional[D]:
        return self._items[-1] if self._items else None
    
    @property
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: D) -> InsertionResult[D]:
        """Each subclass must implement."""
        pass
    
    @abstractmethod
    def search(self, context: C) -> SearchResult[List[D]]:
        """Each subclass must implement."""
        pass
    
    @LoggingLevelRouter.monitor
    def undo(self) -> DeletionResult[D]:
        method = "DataService.undo"
        try:
            if self._items == 0:
                return DeletionResult.failure(
                    PoppingEmptyStackException(f"{method}: {PoppingEmptyStackException.DEFAULT_MESSAGE}")
                )
            item = self._items.pop()
            return DeletionResult.success(payload=item)
        except Exception as ex:
            return DeletionResult.failure(
                DataServiceException(ex=ex, message=f"{method}: {DataServiceException.DEFAULT_MESSAGE}")
            )
    
