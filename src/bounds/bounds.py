# src/bounds/bounds.py

"""
Module: bounds.axis.bounds
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from model import Vector
from register import Axis


class AxisBounds(ABC):
    
    
    @property
    @abstractmethod
    def origin(self) -> Axis:
        pass
    
    @property
    @abstractmethod
    def terminus(self) -> Vector:
        pass