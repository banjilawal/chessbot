# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import (
    Builder, SearchContext, SearchContextService, SearchResult, Service, Validator, SearchService
)

T = TypeVar("T")


class DataService(ABC, Service[Generic[T]]):
    """"""
    _items: [T]
    _search_service: SearchService[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            items: [T],
            builder: Builder[T],
            validator: Validator[T],
            search_service: SearchService[T],
    ):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._items = items
        self._search_service = search_service
    
    @property
    @abstractmethod
    def items(self) -> [T]:
        pass
    
    @property
    @abstractmethod
    def service(self) -> Service[T]:
        pass
    
    @property
    @abstractmethod
    def context_service(self) -> SearchContextService[T]:
    
    @abstractmethod
    def search(self, context: SearchContext) -> SearchResult[[T]]:
        pass