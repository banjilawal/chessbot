# src/ray/bounds/ray.py

"""
Module: ray.bounds.ray
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from model import Vector
from register import VectorRegister


class RayBounds:
    
    _endpoints: VectorRegister
    
    def __init__(self, origin: Vector, terminus: Vector):
        self._endpoints = VectorRegister(u=origin, v=terminus)
        
    @property
    def origin(self) -> Vector:
        return self._endpoints.u
    
    @property
    def terminus(self) -> Vector:
        return self._endpoints.v