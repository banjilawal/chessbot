# src/blueprint/space/quadrant/blueprint.py

"""
Module: blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from fabrication.blueprint import QuadrantBlueprint
from err import NortheastQuadrantNullException
from domain.model import Vector
from space import NortheastQuadrant


class NortheastQuadrantBlueprint(QuadrantBlueprint[NortheastQuadrant]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a NortheastQuadrant.


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
            model_class: Type[NortheastQuadrant] = NortheastQuadrant,
            null_exception: Optional[NortheastQuadrantNullException] | None = None,
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
            null_exception=null_exception or NortheastQuadrantNullException(),
        )
    
    @property
    def model_class(self) -> Type[NortheastQuadrant]:
        return cast(Type[NortheastQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> NortheastQuadrantNullException:
        return cast(NortheastQuadrantNullException, super().null_exception)