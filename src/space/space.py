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


class Space(ABC):
    
    _terminus: Vector
    
    def __init__(self, terminus: Vector):
        self._terminus = terminus
    
    
    @property
    @abstractmethod
    def terminus(self) -> Vector:
        return self._terminus
    