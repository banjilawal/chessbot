# src/logic/system/search/query/stack.py

"""
Module: logic.system.search.query.stack
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from typing import Generic, List, TypeVar

from logic.system import Query
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
    
    
