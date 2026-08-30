# src/domain/search/context.py

"""
Module: domain.search.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Any, Dict, Generic, Optional, TypeVar
from abc import ABC, abstractmethod

from domain import Searchable

T = TypeVar("T", bound="Searchable")


class Context(ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply an attribute-value tuple used to search a DomainObjectCollection.
                
    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_size: int
        
    Provides:
        - def to_dict() -> Dict[str, Any]
        
    Super Class:
    """
    _id: Optional[int]
    _name: Optional[str]
    _max_size: int

    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_size: Optional[int] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            max_size: Optional[int]
        """
        super().__init__()
        self._id = id
        self._name = name
        self._max_size = max_size or 1

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_size(self) -> int:
        return self._max_size
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_above_max_size(self) -> bool:
        return self.size > self._max_size
    
    @property
    def size(self) -> int:
        return len(self.to_dict)

    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Implementations must override."""
        pass