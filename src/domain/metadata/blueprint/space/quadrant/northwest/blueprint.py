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
from err import NorthwestQuadrantNullException
from domain.model import Vector
from space import NorthwestQuadrant


class NorthwestQuadrantBlueprint(QuadrantBlueprint[NorthwestQuadrant]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a NorthwestQuadrant.


     Attributes:
        origin: Vector
        model_class: Type[NorthwestQuadrant]
        null_exception: Optional[NorthwestQuadrantNullException]

     Provides:

     Super Class:
        QuadrantSpaceBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[NorthwestQuadrant] = NorthwestQuadrant,
            null_exception: Optional[NorthwestQuadrantNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            model_class: Type[NorthwestQuadrant]
            null_exception: Optional[NorthwestQuadrantNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception or NorthwestQuadrantNullException(),
        )
    
    @property
    def model_class(self) -> Type[NorthwestQuadrant]:
        return cast(Type[NorthwestQuadrant], super().model_class)
    
    @property
    def null_exception(self) -> NorthwestQuadrantNullException:
        return cast(NorthwestQuadrantNullException, super().null_exception)