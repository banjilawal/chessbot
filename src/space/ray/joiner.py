# src/space/ray/space/ray.py

"""
Module: space.ray.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
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
        4.  No direct access to the list.
  
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
    
    def __init__(self, points: Optional[List[T]]):
            self._points = points or []
        
    @property
    def origin(self) -> Optional[T]:
        if self.is_empty: return None
        return self._points[0]
    
    @property
    def terminus(self) -> Optional[T]:
        if self.is_empty: return None
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
    
    def add_point(self, point: T):
        self._points.append(point)
    
    @property
    def is_cycle(self) -> bool:
        """
        Avoids duplicating tests for empty or size == 1 rays.

        Action:
            Returns False if either:
                -   is empty
                -   has one item
            Otherwise, returns True.
        Note:
            Subclasses must implement other tests for cycles.
        Returns:
            bool
        """
        if self.is_empty:
            return False
        if self.size == 1:
            return False
        return True
        

    def have_same_origin(self, other) -> bool:
        """
        Avoids duplicating tests sameness, null and type checks before
        performing additional, definitive tests in subclasses.

        Action:
            Returns False if either:
                -   other is null
                -   other is not a Ray
                -   either ray is empty
            Returns True is either:
                -   other is self
                -   other is a Ray.
        Note:
            Subclasses must implement other tests for equal origins.
        Returns:
            bool
        """
        if not self._bool_helper(other):
            return False
        ray = cast(Ray, other)
        return self.is_empty or ray.is_empty
    
    def have_same_terminus(self, other) -> bool:
        """
        Avoids duplicating tests sameness, null and type checks before
        performing additional, definitive tests in subclasses.

        Action:
            Returns False if either:
                -   other is null
                -   other is not a Ray
                -   either ray is empty
            Returns True is either:
                -   other is self
                -   other is a Ray.
        Note:
            Subclasses must implement other tests for equal termini.
        Returns:
            bool
        """
        if not self._bool_helper(other):
            return False
        ray = cast(Ray, other)
        return self.is_empty or ray.is_empty
    
    @abstractmethod
    def is_not_cycle(self) -> bool:
        pass
    
    @abstractmethod
    def origins_are_different(self, other) -> bool:
        pass
        
    @abstractmethod
    def termini_are_different(self, other) -> bool:
        pass
    
    def _bool_helper(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        return isinstance(other, Ray)
        
    
        
    
        