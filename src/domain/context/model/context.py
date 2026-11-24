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

from domain import Context, Model

T = TypeVar("T", bound="Model")


class ModelContext(Context[T], ABC, Generic[T]):
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
        Context
    """
    
    _id: Optional[int]
    _name: Optional[str]

    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            capacity: Optional[int] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            capacity: Optional[int]
        """
        super().__init__(capacity=capacity)
        self._id = id

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Implementations must override."""
        pass