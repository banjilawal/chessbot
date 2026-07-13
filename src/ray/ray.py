# src/ray/ray.py

"""
Module: ray.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import abstractmethod
from typing import List

from model import Vector


class Ray:
    
    @abstractmethod
    def compute(self, coord) -> List[Vector]:
        pass