# src/ray/ray.py

"""
Module: ray.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Iterator, List, Optional, TypeVar, cast

from model import Model

T = TypeVar("T")


class Ray(Model, Generic[T]):
    """
    Role:
        -   DTO
        -   Transform

    Responsibilities:
        1.  Lightweight data structure of elements with 2D addressing.
        2.  Elements are ordered by discovery in a 1D space (line).
        3.  Resource for creating Nodes and Edges in GraphFactory.
  
    Attributes:
        origin: Optional[T]
        terminus: Optional[T]
        iterator: Iterator[T]:
        is_empty: bool
        is_cycle: bool
        size: int

    Provides:
        -   def add_point(point: T)
        -   def have_same_origin(other) -> bool
        -   def origins_are_different(other) -> bool
        -   def have_same_terminus(other) -> bool
        -   def terminus_is_different(other) -> bool

    Super Class:

    WARNING:
        *****===DOES NOT GUARANTEE UNIQUENESS, INTEGRITY OR CONSISTENCY===*****
    """
    _points: List[T]
    
    def __init__(self, origin: Optional[T] | None = None,):
        self._points = []
        if origin is not None:
            self._points.append(origin)
        
    @property
    def origin(self) -> Optional[T]:
        if self.is_empty:
            return None
        return self._points[0]
    
    @property
    def terminus(self) -> Optional[T]:
        if self.is_empty:
            return None
        return self._points[-1]
    
    @property
    def size(self) -> int:
        return len(self._points)
    
    @property
    def iterator(self) -> Iterator[T]:
        return iter(self._points)
    
    @property
    def is_empty(self) -> bool:
        return len(self._points) == 0
    
    @property
    def is_cycle(self) -> bool:
        if self.is_empty:
            return False
        if self.size == 1:
            return False
        return True
    
    def add_point(self, point: T):
        self._points.append(point)
        

    def have_same_origin(self, other) -> bool:
        if not self._bool_helper(other):
            return False
        ray = cast(Ray, other)
        return self.is_empty or ray.is_empty
    
    def origins_are_different(self, other) -> bool:
        return not self.have_same_origin(other)
        
    def have_same_terminus(self, other) -> bool:
        return self.have_same_origin(other)
    
    def terminus_is_different(self, other) -> bool:
        return self.have_same_origin(other)
    
    def _bool_helper(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        return isinstance(other, Ray)
        
    
        
    
        