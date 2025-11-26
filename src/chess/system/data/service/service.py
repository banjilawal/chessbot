# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system.data import DeletionResult, DataServiceException, RemovingNullDataException
from chess.system import (
    Context, DataServiceException, InsertionResult, LoggingLevelRouter, PoppingEmptyStackException, SearchResult,
    Service,
    Search
)


D = TypeVar("D")
C = TypeVar("C", binding=Context)

class DataService(ABC, [Generic [D, C]]):
    """
    # ROLE: Data Stack, Search Service, CRUD Operations, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Scales Builder and Validator operations for collection of objects.
    2.  Provides context aware Search.
    3.  Safe and reliable CRUD operations.
    4.  Public facing API.

    # PROVIDES:
        *   Builder
        *   Validator
        *   Search
        *   Insertion
        *   Deletin

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   items (List[D]):
        *   search (Search[D]):
        *   service (Service[D]):
        *   context_service (Service[C]);
        *   current_item (D):
        *   size (int):
    """
    _id: int
    _size: int
    _name: str
    _items: List[D]
    _search: Search[D]
    _service: Service[D]
    _context_service: Service[C]
    
    _current_item: D

    def __init__(
            self,
            id: int,
            name: str,
            items: List[D],
            search: Search[D],
            service: Service[D],
            context_service: Service[C],
    ):
        self._id = id
        self._name = name
        self._items = items
        self._search = search
        self._service = service
        self._context_service = context_service
        
        self._size = len(self._items)
        self._current_item = self._items[-1] if self._items else None
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def push(self, item: D) -> InsertionResult[D]:
        """Each subclass must implement."""
        pass
    
    @abstractmethod
    def search(self, context: C) -> SearchResult[List[D]]:
        """Each subclass must implement."""
        pass
        
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
    def service(self) -> Service[D]:
        return self._service
    
    @property
    def context_service(self) -> Service[C]:
        return self._context_service
    
    @property
    def current_item(self) -> Optional[D]:
        return self._items[-1] if self._items else None
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    @LoggingLevelRouter.monitor
    def undo(self) -> DeletionResult[D]:
        method = "DataService.undo"
        try:
            if self._items == 0:
                return DeletionResult.failure(
                    PoppingEmptyStackException(
                        f"{method}: "
                        f"{PoppingEmptyStackException.DEFAULT_MESSAGE}"
                    )
                )
            item = self._items.pop()
            return DeletionResult.success(payload=item)
        except Exception as ex:
            return DeletionResult.failure(
                DataServiceException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{DataServiceException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
