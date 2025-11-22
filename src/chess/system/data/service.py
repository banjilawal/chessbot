# src/chess/system/data/service.py

"""
Module: chess.system.data.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from chess.system import Builder, DataResult, SearchContext, SearchResult, Service, Validator

T = TypeVar("T")


class DataService(ABC, Service[Generic[T]]):
    """"""
    _items: [T]
    
    def __init__(self, id: int, name: str, items: [T], builder: Builder[T], validator: Validator[T]):
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._items = items
    
    @property
    def items(self) -> [T]:
        return self._items
    

    @property
    def