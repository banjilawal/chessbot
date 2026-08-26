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
from err import SouthwestQuadrantNullException
from domain.model import Vector
from space import SouthwestQuadrant


class SouthwestQuadrantBlueprint(QuadrantBlueprint[SouthwestQuadrant]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for instantiating a SouthwestQuadrant.


     Attributes:
        origin: Vector
        model_class: Type[SouthwestQuadrant]
        null_exception: Optional[SouthwestQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[SouthwestQuadrant] = SouthwestQuadrant,
            null_exception: Optional[SouthwestQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[SouthwestQuadrant]
            null_exception: Optional[SouthwestQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception or SouthwestQuadrantNullException(),
        )
    
    @property
    def model_class(self) -> Type[SouthwestQuadrant]:
        return cast(Type[SouthwestQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> SouthwestQuadrantNullException:
        return cast(SouthwestQuadrantNullException, super().null_exception)