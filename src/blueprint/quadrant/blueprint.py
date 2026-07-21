# src/blueprint/quadrant/blueprint.py

"""
Module: blueprint.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Type, cast

from blueprint import Blueprint
from space.traversal.quadrant import KnightSpace
from model import Vector


class QuadrantBlueprint(Blueprint, ABC):
    _x_step: int
    _slope: int
    _terminus: Vector
    
    def __init__(self, x_step: int, slope: int, terminus: Vector):
        super().__init__(model_class=Type[KnightSpace])
        self._x_step = x_step
        self._slope = slope
        self._terminus = terminus
    
    @property
    def model_class(self) -> Type[KnightSpace]:
        return cast(Type[KnightSpace], self.model_class)
    
    @property
    def x_step(self) -> int:
        return self._x_step
    
    @property
    def slope(self) -> int:
        return self._slope
    
    @property
    def terminus(self) -> Vector:
        return self._terminus
    
    def quadrant_from_blueprint(self) -> KnightSpace:
        return KnightSpace(
            x_step=self._x_step,
            slope=self._slope,
            terminus=self._terminus
        )
    
    