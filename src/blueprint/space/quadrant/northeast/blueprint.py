# src/blueprint/space/quadrant/blueprint.py

"""
Module: blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Generic, Optional, Type, TypeVar, cast

from blueprint import QuadrantBlueprint, SpaceBlueprint
from err import NortheastQuadrantNullException, QuadrantNullException
from model import Vector
from space import NortheastQuadrant, Space, QuadrantSpace


class NortheastQuadrantBlueprint(QuadrantBlueprint[NortheastQuadrant]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a QuadrantSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[NortheastQuadrant]
        null_exception: Optional[NortheastQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[NortheastQuadrant],
            null_exception: Optional[NortheastQuadrantNullException] |
                            None = NortheastQuadrantNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[NortheastQuadrant]
            null_exception: Optional[NortheastQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
        
    
    @property
    def model_class(self) -> Type[NortheastQuadrant]:
        return cast(Type[NortheastQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> NortheastQuadrantNullException:
        return cast(NortheastQuadrantNullException, super().null_exception)