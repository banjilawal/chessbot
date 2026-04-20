# src/model/blueprint/vector/model.py

"""
Module: model.blueprint.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Blueprint, Vector


class VectorBlueprint(Blueprint[Vector]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides values for instantiating a Vector object.

    Attributes:
        x: int
        y: int
            
    Provides:

     Super Class:
        Blueprint
     """
    _x: int
    _y: int
    
    def __init__(self, x: int, y: int,):
        """
        Args:
            x: int
            y: int
        """
        super().__init__()
        self._x = int
        self._y = int

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y