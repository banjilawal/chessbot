# src/logic/span/ray/ray.py

"""
Module: logic.span.ray.ray
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

T = TypeVar('T')

class Ray(ABC, Generic[T]):
    """
    # ROLE: Data-Holder
    
    # RESPONSIBILITIES:
    1.  Stores members that define a ray from an origin to a terminus

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: Coord
        *   members: List[Coord]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: Coord
        *   members: List[Coord]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    _origin: T
    _members: List[T]
    
    def __init__(self, origin: T, members: List[T]):
        """
        Args:
            origin: Coord
            members: List[Coord]
        """
        self._origin = origin
        self._members = members
        
    @property
    def origin(self) -> T:
        return self._origin
    
    @property
    def members(self) -> List[T]:
        return self._members
    
    @property
    def ray_length(self) -> int:
        return len(self._members) + 1
    
    @property
    def is_empty(self) -> bool:
        return len(self._members) == 0