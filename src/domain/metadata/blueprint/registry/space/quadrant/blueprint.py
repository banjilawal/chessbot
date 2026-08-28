# src/domain/metadata/blueprint/space/reservoir/quadrant/blueprint

"""
Module: domain.metadata.blueprint.space.reservoir.quadrant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import SpaceReservoirBlueprint
from err import QuadrantReservoirNullException

from domain.model import Vector
from space import Quadrant, QuadrantReservoir


class QuadrantReservoirBlueprint(SpaceReservoirBlueprint[Quadrant]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating a QuadrantReservoir object.

     Attributes:
        origin: Vector,
        terminus: Optional[Vector] | None = None,
        domain_class: Type[QuadrantReservoir] = QuadrantReservoir,
        domain_null_exception: Optional[QuadrantReservoirNullException]

     Provides:

     Super Class:
        SpaceReservoirBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            domain_class: Type[QuadrantReservoir] = QuadrantReservoir,
            domain_null_exception: Optional[QuadrantReservoirNullException] | None = None,
    ):
        """
        Args:
            origin: Vector,
            domain_class: Type[QuadrantReservoir] = QuadrantReservoir,
            domain_null_exception: Optional[QuadrantReservoirNullException]
        """
        super().__init__(
            origin=origin,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or QuadrantReservoirNullException(),
        )
    
    @property
    def domain_class(self) -> Type[QuadrantReservoir]:
        return cast(Type[QuadrantReservoir], super().domain_class)
    
    @property
    def domain_null_exception(self) -> QuadrantReservoirNullException:
        return cast(QuadrantReservoirNullException, super().domain_null_exception)