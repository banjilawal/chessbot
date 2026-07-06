# src/context/model/state.py

"""
Module: context.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

@dataclass
class Context(ABC, Generic[T]):
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
    _id: Optional[int] = None
    _name: Optional[str] = None

    def __init__(self, id: Optional[int] | None = None, name: Optional[str] | None = None):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
        """
        self._id = id
        self._name = name

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    @abstractmethod
    def to_dict(self) -> dict:
        """Implementations must override."""
        pass