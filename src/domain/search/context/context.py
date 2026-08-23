# src/domain/search/context/context.py.py

"""
Module: domain.search.context.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod

from domain import DomainObject, DomainSearchObject

T = TypeVar("T", bound="DomainObject")


class SearchContext(DomainSearchObject, ABC, Generic[T]):
    """
    Role:
        -   Selection
        -   Routing mask

    Responsibilities:
        1.  Supply the criteria a Searcher uses to find a hit in a DomainObjectCollection.
                
    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_activated_filters: Optional[int]
        
    Provides:
        -   to_dict() -> Dict[str, Any]
        
    Super Class:
    """
    _id: Optional[int]
    _name: Optional[str]
    _max_activated_filters: int

    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_activated_filters: Optional[int] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            max_activated_filters: Optional[int]
        """
        super().__init__()
        self._id = id
        self._name = name
        self._max_activated_filters = max_activated_filters or 1

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_activated_filters(self) -> int:
        return self._max_activated_filters
    
    @property
    def no_active_filters(self) -> bool:
        return self.activated_filters == 0
    
    @property
    def excess_active_filters(self) -> bool:
        return self.activated_filters > self._max_activated_filters
    
    @property
    def activated_filters(self) -> int:
        return len(self.to_dict)

    @property
    @abstractmethod
    def to_dict(self) -> dict:
        """Implementations must override."""
        pass