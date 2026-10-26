# src/collection/collection.py

"""
Module: collection.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar

from domain import DomainDataObject

T = TypeVar("T")

class DataStruct(ABC, Generic[T]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Interface for defining reliable and safe, domain-specific data structures.

    Attributes:
        size: int
        is_empty: bool
        is_not_empty: bool
        iterator: Iterator[T]

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
    
    @property
    @abstractmethod
    def iterator(self) -> Iterator[T]:
        pass
