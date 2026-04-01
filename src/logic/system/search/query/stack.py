

from __future__ import annotations
from abc import ABC
from typing import Generic, List, TypeVar

from logic.system.search import Context


T = TypeVar("T")

class StackQuery(Query, Generic[T]):
    _dataset: List[T]
    
    def __init__(self, dataset: List[T], context: Context[T]):
        """
        Args:
            dataset: List[T]
            context: Context[T]
        """
        super().__init__(context=context)
        self._dataset = dataset
        
    @property
    def dataset(self) -> List[T]:
        return self._dataset
    
    
