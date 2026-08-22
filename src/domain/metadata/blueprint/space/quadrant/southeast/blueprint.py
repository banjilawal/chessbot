# src/domain/metadata/blueprint/space/quadrant/blueprint.py

"""
Module: domain.metadata.blueprint.space.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import QuadrantBlueprint
from err import SoutheastQuadrantNullException
from domain.model import Vector
from space import SoutheastQuadrant


class SoutheastQuadrantBlueprint(QuadrantBlueprint[SoutheastQuadrant]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a SoutheastQuadrant.


     Attributes:
        origin: Vector
        model_class: Type[SoutheastQuadrant]
        null_exception: Optional[SoutheastQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[SoutheastQuadrant] = SoutheastQuadrant,
            null_exception: Optional[SoutheastQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[SoutheastQuadrant]
            null_exception: Optional[SoutheastQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception or SoutheastQuadrantNullException(),
        )
    
    @property
    def model_class(self) -> Type[SoutheastQuadrant]:
        return cast(Type[SoutheastQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> SoutheastQuadrantNullException:
        return cast(SoutheastQuadrantNullException, super().null_exception)