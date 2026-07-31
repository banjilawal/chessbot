# src/blueprint/space/reservoir/quadrant/blueprint

"""
Module: blueprint.space.reservoir.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, Type, cast

from blueprint import SpaceReservoirBlueprint
from err import QuadrantReservoirNullException

from model import Vector
from geometry.space import Quadrant, QuadrantReservoir


class QuadrantReservoirBlueprint(SpaceReservoirBlueprint[Quadrant]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a QuadrantReservoir object.

     Attributes:
        origin: Vector,
        terminus: Optional[Vector] | None = None,
        model_class: Type[QuadrantReservoir] = QuadrantReservoir,
        null_exception: Optional[QuadrantReservoirNullException]

     Provides:

     Super Class:
        SpaceReservoirBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            model_class: Type[QuadrantReservoir] = QuadrantReservoir,
            null_exception: Optional[QuadrantReservoirNullException] | None = None,
    ):
        """
        Args:
            origin: Vector,
            model_class: Type[QuadrantReservoir] = QuadrantReservoir,
            null_exception: Optional[QuadrantReservoirNullException]
        """
        super().__init__(
            origin=origin,
            model_class=model_class,
            null_exception=null_exception or QuadrantReservoirNullException(),
        )
    
    @property
    def model_class(self) -> Type[QuadrantReservoir]:
        return cast(Type[QuadrantReservoir], super().model_class)
    
    @property
    def null_exception(self) -> QuadrantReservoirNullException:
        return cast(QuadrantReservoirNullException, super().null_exception)