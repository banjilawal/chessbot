# src/space/space.py

"""
Module: space.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from model import Vector
from space import SpaceBounds


class Space(ABC):
    _bounds: SpaceBounds
    
    def __init__(self, bounds: SpaceBounds):
        self._bounds = bounds
    
    @property
    def bounds(self) -> SpaceBounds:
        return self._bounds
    
    @property
    @abstractmethod
    def origin(self) -> Vector:
        pass
    
    @property
    @abstractmethod
    def terminus(self) -> Vector:
        pass
    