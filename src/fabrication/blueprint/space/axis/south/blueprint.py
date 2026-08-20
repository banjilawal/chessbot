# src/blueprint/space/axis/blueprint.py

"""
Module: blueprint.space.axis.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from fabrication.blueprint import AxisBlueprint
from err import SouthAxisNullException
from model import Vector
from space import SouthAxis


class SouthAxisBlueprint(AxisBlueprint[SouthAxis]):
    """
     Role:
         -   DTO

     Responsibilities:
         1.  Provides values for instantiating a SouthAxis.


     Attributes:
        origin: Vector
        model_class: Type[SouthAxis]
        null_exception: Optional[SouthAxisNullException]

     Provides:

     Super Class:
        AxisBlueprint
     """
    
    def __init__(
            self,
            origin: Vector,
            terminus: Optional[Vector] | None = None,
            model_class: Type[SouthAxis] = SouthAxis,
            null_exception: Optional[SouthAxisNullException] | None = None,
    ):
        """
        Args:
            origin: Vector
            terminus: Optional[Vector]
            model_class: Type[WestAxis]
            null_exception: Optional[WestAxisNullException]
        """
        super().__init__(
            origin=origin,
            terminus=terminus,
            model_class=model_class,
            null_exception=null_exception or SouthAxisNullException(),
        )
    
    @property
    def model_class(self) -> Type[SouthAxis]:
        return cast(Type[SouthAxis], super().model_class)
    
    @property
    def null_exception(self) -> SouthAxisNullException:
        return cast(SouthAxisNullException, super().null_exception)