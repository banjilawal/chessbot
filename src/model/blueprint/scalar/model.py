# src/model/blueprint/scalar/model.py

"""
Module: model.blueprint.scalar.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Blueprint, Scalar


class ScalarBlueprint(Blueprint[Scalar]):
    """
    Role:
        -   Container

    Responsibilities:
        1.  Provides magnitude value for instantiating a Scalar object.

    Attributes:
        magnitude: int
        
    Provides:

     Super Class:
        Blueprint
     """
    _magnitude: int
    
    def __init__(
            self,
            magnitude: int,
    ):
        """
        Args:
            magnitude: Optional[int]
        """
        super().__init__()
        self._magnitude = magnitude
        
    @property
    def magnitude(self) -> int:
        return self._magnitude
