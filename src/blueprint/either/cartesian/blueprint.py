# src/blueprint/either/cartesian/blueprint.py

"""
Module: blueprint.either.cartesian.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Optional, Type, cast

from blueprint import EitherBlueprint
from model import Coord, Vector
from chooser import CartesianPoint



class CartesianPointBlueprint(EitherBlueprint[CartesianPoint]):
    """
    Role:
        -   Container
    
    Responsibilities:
        1.  Provides values for instantiating a CartesianEither object.
    
    Attributes:
        vector: Optional[Vector]
        coord: Optional[Coord]
        model_class: Type[CartesianPoint]
    
    Provides:
    
    Super Class:
        EitherBlueprint
    """
    _vector: Optional[Vector]
    _coord: Optional[Coord]
    
    def __init__(
            self,
            coord: Optional[Coord] | None = None,
            vector: Optional[Vector] | None = None,
            model_class: Type[CartesianPoint] = CartesianPoint,
    ):
        """
        Args:
            vector: Optional[Vector]
            coord: Optional[Coord]
            model_class: Type[CartesianPoint]
        """
        super().__init__(model_class=model_class)
        self._coord = coord
        self._vector = vector
    
    @property
    def model_class(self) -> Type[CartesianPoint]:
        return cast(Type[CartesianPoint], self.model_class)
    
    @property
    def coord(self) -> Optional[Coord]:
        return self._coord
    
    @property
    def vector(self) -> Optional[Vector]:
        return self._vector
    
    

