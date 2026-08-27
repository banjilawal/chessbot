# src/topology/registry/space/space.py

"""
Module: topology.registry.space.space
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

from domain.model import Vector

T = TypeVar("T", bound="Space")


class SpaceReservoir(ABC, Generic[T]):
    """
    Role:
        - Selection
        -  Iterator
        -  Routing Mask

    Responsibilities:
        1.  Interface for implementing an iterator that preserves type when looping through
            an origin's spaces.

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
    def space_type_dict(self) -> Dict[Type[T], T]:
        pass

