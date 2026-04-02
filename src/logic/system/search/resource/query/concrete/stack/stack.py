# src/logic/system/search/resource/query/concrete/stack.py

"""
Module: logic.system.search.resource.query.concrete.stack
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, TypeVar

from logic.system import Query
from logic.system.search import Context


T = TypeVar("T")

class StackQuery(Query, Generic[T]):
    _stack: List[T]
    
    def __init__(self, stack: List[T], context: Context[T]):
        """
        Args:
            stack: List[T]
            context: Context[T]
        """
        super().__init__(context=context)
        self._stack = stack
        
    @property
    @abstractmethod
    def stack(self) -> List[T]:
        pass
    
    
