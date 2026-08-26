# src/domain/search/context.py

"""
Module: domain.search
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from ast import Dict
from typing import Any, Generic, Optional, TypeVar
from abc import ABC, abstractmethod

from domain import Searchable

T = TypeVar("T", bound="Searchable")


class SearchContext(ABC, Generic[T]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply the criteria a Searcher uses to find a hit in a DomainObjectCollection.
                
    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_activated_contexts: int
        
    Provides:
        -   to_dict() -> Dict[str, Any]
        
    Super Class:
    """
    _id: Optional[int]
    _name: Optional[str]
    _max_activated_contexts: int

    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_activated_contexts: Optional[int] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            max_activated_contexts: Optional[int]
        """
        super().__init__()
        self._id = id
        self._name = name
        self._max_activated_contexts = max_activated_contexts or 1

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_activated_contexts(self) -> int:
        return self._max_activated_contexts
    
    @property
    def has_no_active_context(self) -> bool:
        return self.active_context_count == 0
    
    @property
    def has_excessive_active_contexts(self) -> bool:
        return self.active_context_count > self._max_activated_contexts
    
    @property
    def active_context_count(self) -> int:
        return len(self.to_dict)

    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Implementations must override."""
        pass