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
from err import southeastQuadrantNullException, QuadrantNullException
from model import Vector
from space import southeastQuadrant, Space, QuadrantSpace


class southeastQuadrantBlueprint(QuadrantBlueprint[southeastQuadrant]):
    """
     Role:
         -   Container
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a QuadrantSpace object.
         2.  DTO

     Attributes:
        origin: Vector
        model_class: Type[southeastQuadrant]
        null_exception: Optional[southeastQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[southeastQuadrant],
            null_exception: Optional[southeastQuadrantNullException] |
                            None = southeastQuadrantNullException(),
    ):
        """
        Args:
            origin: Vector
            model_class: Type[southeastQuadrant]
            null_exception: Optional[southeastQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception
        )
        
    
    @property
    def model_class(self) -> Type[southeastQuadrant]:
        return cast(Type[southeastQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> southeastQuadrantNullException:
        return cast(southeastQuadrantNullException, super().null_exception)