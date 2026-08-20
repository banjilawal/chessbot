# src/blueprint/space/reservoir/axis/blueprint

"""
Module: blueprint.space.reservoir.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from fabrication.blueprint import SpaceReservoirBlueprint
from err import AxisReservoirNullException

from model import Vector
from topology.registry import AxisReservoir



class AxisReservoirBlueprint(SpaceReservoirBlueprint[AxisReservoir]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating an AxisReservoir object.

     Attributes:
        origin: Vector,
        terminus: Optional[Vector] | None = None,
        model_class: Type[AxisReservoir] = AxisReservoir,
        null_exception: Optional[AxisReservoirNullException]

     Provides:

     Super Class:
        SpaceReservoirBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            model_class: Type[AxisReservoir] = AxisReservoir,
            null_exception: Optional[AxisReservoirNullException] | None = None,
    ):
        """
        Args:
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            model_class: Type[AxisReservoir] = AxisReservoir,
            null_exception: Optional[AxisReservoirNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            model_class=model_class,
            null_exception=null_exception or AxisReservoirNullException(),
        )
    
    @property
    def space_class(self) -> Type[AxisReservoir]:
        return cast(Type[AxisReservoir], super().model_class)
    
    @property
    def null_exception(self) -> AxisReservoirNullException:
        return cast(AxisReservoirNullException, super().null_exception)