# src/blueprint/toggle/vector/blueprint.py

"""
Module: blueprint.toggle.vector.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Optional, Type, cast

from blueprint import ToggleBlueprint
from model import Coord, Vector
from toggle import VectorToggle


class VectorToggleBlueprint(ToggleBlueprint[VectorToggle]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a VectorToggle object.
    
    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]
        model_class: Type[VectorToggle]
    
    Provides:
    
    Super Class:
        ToggleBlueprint
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            coord: Optional[Coord] | None = None,
            vector: Optional[Vector] | None = None,
            model_class: Type[VectorToggle] = VectorToggle,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
            model_class: Type[VectorToggle]
        """
        super().__init__(model_class=model_class)
        self._coord = coord
        self._vector = vector
    
    @property
    def model_class(self) -> Type[VectorToggle]:
        return cast(Type[VectorToggle], super().model_class)
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def vector(self) -> Optional[Vector]:
        return self._vector
    
    

