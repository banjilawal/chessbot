# src/space/reservoir/space.py

"""
Module: space.reservoir.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from model import Vector

T = TypeVar("T", bound="Space")


class SpaceReservoir(ABC, Generic[T]):
    """
    Role:
        -   Selection
        -   Routing mask

    Responsibilities:
        1.  Interface for creating Space selecting objects.

    Attributes:
        size: int
        origin: Vector
        iterator: iter
        is_empty: bool
        is_not_empty: bool

    Provides:
   
    Super Class:
    """
    _origin: Vector

    def __init__(self, origin: Vector):
        """
        Args:
            origin: Vector
        """
        self._origin = origin
        
    @property
    def origin(self) -> Vector:
        return  self._origin
    
    
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
    def iterator(self) -> iter:
        pass
