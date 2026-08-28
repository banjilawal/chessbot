# src/domain/metadata/blueprint/space/reservoir/axis/blueprint

"""
Module: domain.metadata.blueprint.space.reservoir.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import SpaceReservoirBlueprint
from err import AxisReservoirNullException

from domain.model import Vector
from topology.registry import AxisReservoir



class AxisReservoirBlueprint(SpaceReservoirBlueprint[AxisReservoir]):
    """
     Role:
         -  DTO

     Responsibilities:
         1.  Provides values for hydrating an AxisReservoir object.

     Attributes:
        origin: Vector,
        terminus: Optional[Vector] | None = None,
        domain_class: Type[AxisReservoir] = AxisReservoir,
        domain_null_exception: Optional[AxisReservoirNullException]

     Provides:

     Super Class:
        SpaceReservoirBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[AxisReservoir] = AxisReservoir,
            domain_null_exception: Optional[AxisReservoirNullException] | None = None,
    ):
        """
        Args:
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            domain_class: Type[AxisReservoir] = AxisReservoir,
            domain_null_exception: Optional[AxisReservoirNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            domain_class=domain_class,
            domain_null_exception=domain_null_exception or AxisReservoirNullException(),
        )
    
    @property
    def space_class(self) -> Type[AxisReservoir]:
        return cast(Type[AxisReservoir], super().domain_class)
    
    @property
    def domain_null_exception(self) -> AxisReservoirNullException:
        return cast(AxisReservoirNullException, super().domain_null_exception)