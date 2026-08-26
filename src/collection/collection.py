# src/collection/collection.py

"""
Module: collection.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from domain import DomainDataObject

T = TypeVar("T", bound="DomainDataObject")

class DomainObjectCollection(ABC, Generic[T]):
    """
    Role:
        -  Data Holder
        -  Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        items: Tuple[T, ...]

    Provides:

    Super Class:
    """
    def __init__(self):
        pass
    
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_empty(self) -> bool:
        pass
