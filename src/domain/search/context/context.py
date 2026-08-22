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
        -   Data-Holder

    Responsibilities:
        1.  Supply an attribute-value tuple for selecting an execution path.
                
    Attributes:
        id: Optional[int]
        name: Optional[str]
        max_enabled_toggles: Optional[int]
        
    Provides:
        -   to_dict() -> Dict[str, Any]
        
    Super Class:
    
    Notes:
        1.  Attribute is an entity's property.
        2.  Attribute is routing key.
        3.  Execution logic performed on attribute value.
        
        4.  Why Not Union:
                Used optional attributes with null default values instead of a union type because:
                    -   It's easier to extend
                    -   Implementations can decide if context can be mutually exclusive or not.
                    -   Unions are clunky if there are many attributes.
                    -   Unions don't lower validation and build integrity overhead.
    """
    _id: Optional[int]
    _name: Optional[str]
    _max_enabled_toggles: Optional[int]

    def __init__(
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            max_enabled_toggles: Optional[int] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            max_enabled_toggles: Optional[int]
        """
        super().__init__()
        self._id = id
        self._name = name
        self._max_enabled_toggles = max_enabled_toggles or 1

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name
    
    @property
    def max_enabled_toggles(self) -> int:
        return self._max_enabled_toggles
    
    @property
    def no_active_toggles(self) -> bool:
        return self.active_toggles == 0
    
    @property
    def excess_active_toggles(self) -> bool:
        return self.active_toggles > self._max_enabled_toggles
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)

    @property
    @abstractmethod
    def to_dict(self) -> dict:
        """Implementations must override."""
        pass