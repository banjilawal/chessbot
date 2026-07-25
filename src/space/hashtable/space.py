# src/space/hashtable/space.py

"""
Module: space.hashtable.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Optional, Tuple, Type, TypeVar

from model import Vector
from space import Space

T = TypeVar("T", bound="Space")


class SpaceHashSet(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Store a set of space relations to run as a job.

    Attributes:
        space_set: Tuple[Space, ...]
        
    Provides:

    Super Class:
    """
    _origin: Vector

    
    def __init__(self, origin: Vector, hash_table: Optional[Dict[str, T]] | None = None):
        """
        Args:
            origin: Vector
            hash_table: Optional[Dict[str, T]]
        """
        self._origin = origin
        
    @property
    def origin(self) -> Vector:
        return  self._origin
    
    @property
    @abstractmethod
    def hash_table(self) -> Dict[str, T]:
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
