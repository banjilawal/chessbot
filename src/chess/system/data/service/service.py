# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from chess.system import Context, SearchResult, Service, Search


A = TypeVar("T")
C = TypeVar("C", binding=Context)

class DataService(ABC, [Generic [A,C]]):
    """"""
    _id: int
    _size: int
    _name: str
    _items: List[A]
    _search: Search[A]
    _service: Service[A]
    _context_service: Service[C]
    
    _current_item: A

    
    def __init__(
            self,
            id: int,
            name: str,
            items: List[A],
            search: Search[A],
            service: Service[A],
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
    def items(self) -> List[A]:
        return self._items
    
    @property
    def service(self) -> Service[A]:
        return self._service
    
    @property
    def context_service(self) -> Service[C]:
        return self._context_service
    
    @property
    def current_item(self) -> Optional[A]:
        return self._items[-1] if self._items else None
    
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    @abstractmethod
    def query(self, context: C) -> SearchResult[List[A]]:
        pass