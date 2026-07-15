# src/model/ray/model.py

"""
Module: model.ray.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Iterator, List, Optional, TypeVar

from model import Model

T = TypeVar("T")


class Ray(Model, Generic[T]):
    _points: List[T]
    
    def __init__(self, origin: T):
        self._points = []
        self._points.append(origin)
        
    @property
    def origin(self) -> Optional[T]:
        return self._points[0]
    
    @property
    def terminus(self) -> Optional[T]:
        return self._points[-1]
    
    @property
    def is_empty(self) -> bool:
        return len(self._points) == 0
    
    @property
    def size(self) -> int:
        return len(self._points)
    
    @property
    def iterator(self) -> Iterator[T]:
        return iter(self._points)
    
    def add_point(self, point: T):
        self._points.append(point)
        
    
        
    
        