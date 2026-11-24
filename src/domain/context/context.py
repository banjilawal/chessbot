# src/domain/context/context.py

"""
Module: domain.context.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Any, Dict, Generic, Optional, TypeVar
from abc import ABC, abstractmethod


T = TypeVar("T")


class Context(ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply an attribute-value tuple used to search a DomainObjectCollection.
                
    Attributes:
        capacity: int
        id: Optional[int]
        name: Optional[str]
        
    Provides:
        -   def to_dict() -> Dict[str, Any]
        
    Super Class:
    """
    
    _capacity: int

    def __init__(
            self,
            capacity: Optional[int] | None = None,
    ):
        """
        Args:
            capacity: Optional[int]
        """
        super().__init__()
        self._capacity = capacity or 1

    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def exceeds_capacity(self) -> bool:
        return self.size > self._capacity
    
    @property
    def size(self) -> int:
        return len(self.to_dict)

    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Implementations must override."""
        pass