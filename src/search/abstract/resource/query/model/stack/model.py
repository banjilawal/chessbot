# src/logic/system/search/resource/context/concrete/schema.py

"""
Module: logic.system.search.resource.context.concrete.schema
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Generic, List, TypeVar

from system import Query
from system import Context


T = TypeVar("T")

class StackQuery(Query, Generic[T]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

    Responsibilities:
        1.  Contains
                -   The entity list[T]
                -   The criteria for searching the list
        2.  Delivers it's contents to SearchRouter[T]
        

    Attributes:
        stack: List[T]
        context: Context[T]

    Provides:

    Super Class:
        Query
    """
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
    
    
